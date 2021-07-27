from coleta import download_status

from pymongo import MongoClient
import requests
import time

# Creates client with default server and port
client = MongoClient()

# Get database "wikipedia"
db = client.wikipedia

# Exemplo url: # https://pt.wikipedia.org/w/api.php?action=query&format=json&list=categorymembers&cmtitle=Category%3AArgentina&cmlimit=200
class WikipediaDownloader:
    def __init__(self) -> None:
        self.__url_base = 'https://pt.wikipedia.org/w/api.php'
        self.__f = { 
            'action': 'query',
            'format': 'json',
            'list': 'categorymembers',
            'cmlimit': '200',
            'cmprop': 'ids|title|type'
        }
    
    def __parameters_category_members(self, cmtitle = None, cmpageid = -1):
        fc = self.__f.copy()
        if cmpageid != -1:
            fc['cmpageid'] = cmpageid
        else:
            fc['cmtitle'] = cmtitle
        return fc

    def get_category(self, cmtitle = None, cmpageid = -1):
        params_category = self.__parameters_category_members(cmtitle, cmpageid)
        category_r = requests.get(self.__url_base, params=params_category)
        category_content = []
        if category_r.status_code == 200:
            category_content = category_r.json()
        return category_content

    def get_category_members(self, cmtitle = None, cmpageid = -1):
        return self.get_category(cmtitle=cmtitle, cmpageid=cmpageid)['query']['categorymembers']

class CategoriaCollector:

    def __init__(self, collection_categorias, pagina_collector) -> None:
        self.collection = db[collection_categorias]
        self.wikipedia_downloader = WikipediaDownloader()
        self.pagina_collector = pagina_collector

    def __get_categories_for_status(self, status):
        status_criteria = { 'download': status }
        return list(self.collection.find(status_criteria))

    def get_categories_for_check(self):
        return self.__get_categories_for_status(download_status.CHECK)

    def get_categories_for_download(self):
        waiting_criteria = { 'download': download_status.WAITING }
        return list(self.collection.find(waiting_criteria))

    def add_categories_for_check(self, categories_for_check):
        self.__add_categories_for_status(categories_for_check, download_status.CHECK)

    def __add_categories_for_status(self, categories_for_status, status):
        if len(categories_for_status) > 0:
            for category_for_status in categories_for_status:
                category_for_status['download'] = status
            self.collection.insert_many(categories_for_status)

    def set_categories_for_download(self, pageids):
        for p in pageids:
            self.add_category_for_download(p)

    def set_categories_for_skeep(self, pageids):
        for p in pageids:
            self.__set_category_status(p, download_status.SKEEP)

    # Nome errado. Trocar para set
    def add_category_for_download(self, pageid):
        self.__set_category_status(pageid, download_status.WAITING)

    def __category_exists(self, cmpageid):
        return self.collection.count_documents({'pageid': cmpageid}) > 0

    def __set_category_status(self, pageid, status):
        self.collection.update_one(
            { "pageid": pageid },
            { "$set": { 'download': status } }
        )

    def __set_category_done(self, pageid):
        self.__set_category_status(pageid, download_status.DONE)

    def download_category_tree(self, category, country):
        # Sleep for 1 second before starting download one category tree
        time.sleep(1)

        cmpageid = category['pageid']
        cmtitle = category["title"]
        print(f'Retrieving pages for category {cmtitle} [{cmpageid}]')
        
        members = self.wikipedia_downloader.get_category_members(cmpageid=cmpageid)
        pages = [m for m in members if m['type'] == 'page']
        for p in pages:
            p['country'] = country
        self.pagina_collector.insert_pages(pages, cmpageid, cmtitle)
        subcats = [m for m in members if m['type'] == 'subcat']
        for s in subcats:
            s['parent'] = cmpageid
            s['country'] = country
        subcats_for_check = [s for s in subcats if not self.__category_exists(s['pageid'])]
        self.add_categories_for_check(subcats_for_check)
        self.__set_category_done(cmpageid)

# https://en.wikipedia.org/w/api.php?action=parse&format=json&pageid=3276454&prop=wikitext&formatversion=2
class PaginaCollector:
    
    def __init__(self, collection_paginas, collection_paginas_conteudo) -> None:
        self.collection = db[collection_paginas]
        self.collection_conteudo = db[collection_paginas_conteudo]
        self.__url_base = 'https://pt.wikipedia.org/w/api.php'
        self.__f_page = { 
            'action': 'parse',
            'format': 'json',
            'formatversion': '2'
        }

    def insert_pages(self, pages, cmpageid, cmtitle):
        if len(pages) > 0:
            for page in pages:
                page['category_id'] = cmpageid
                page['category_title'] = cmtitle
                page['download'] = 'Waiting'
            self.collection.insert_many(pages)

    def set_pages_for_wikitext_download(self):
        self.collection.update_many(
            {},
            { '$set': { 'download': 'Waiting' } }
        )

    def set_pages_for_text_download(self):
        self.collection.update_many(
            {},
            { '$set': { 'download_text': 'Waiting' } }
        )

    def get_pages_for_download(self, limite=100):
        return list(self.collection.find({ 'download': download_status.WAITING }).limit(limite))

    def get_pages_for_text_download(self, limite=100):
        return list(self.collection.find({ 'download_text': download_status.WAITING }).limit(limite))

    def get_pages_downloads_counts(self):
        return list(self.collection.aggregate([
            { '$group': { '_id': '$download', 'total': { '$sum': 1 } } }
        ]))

    def get_pages_text_downloads_counts(self):
        return list(self.collection.aggregate([
            { '$group': { '_id': '$download_text', 'total': { '$sum': 1 } } }
        ]))

    def parameters_wikitext(self, pageid):
        fc = self.__f_page.copy()
        fc['pageid'] = pageid
        fc['prop'] = 'wikitext'
        return fc

    def parameters_text(self, pageid):
        fc = self.__f_page.copy()
        fc['pageid'] = pageid
        fc['prop'] = 'text'
        return fc

    def get_wikitext(self, pageid):
        params_wikitext = self.parameters_wikitext(pageid)
        wikitext_r = requests.get(self.__url_base, params=params_wikitext)
        wikitext_content = {}
        if wikitext_r.status_code == 200:
            wikitext_content = wikitext_r.json()
        else:
            print(f'Erro ao fazer download de wikitext de pagina {pageid}')
        return wikitext_content

    def get_text(self, pageid):
        params_text = self.parameters_text(pageid)
        text_r = requests.get(self.__url_base, params=params_text)
        text_content = {}
        if text_r.status_code == 200:
            text_content = text_r.json()
        else:
            print(f'Erro ao fazer download de text de pagina {pageid}')
        return text_content

    def copy_page_with_wikitext(self, page):
        p_wikitext = page.copy()
        p_wikitext['wikitext'] = self.get_wikitext(page['pageid'])['parse']['wikitext']
        return p_wikitext

    def run_wikitext_download(self, amount_wikitext=100):
        pages_for_wikitext_download = self.get_pages_for_download(amount_wikitext)
        print(f'Running wikitext download for {len(pages_for_wikitext_download)} pages')
        current = 1
        for page in pages_for_wikitext_download:
            page_wikitext = self.copy_page_with_wikitext(page)
            del page_wikitext['_id']
            self.collection_conteudo.insert_one(page_wikitext)
            self.collection.update_many(
                { 'pageid': page['pageid'] },
                { '$set': { 'download': download_status.DONE }}
            )
            print(f'Page [{page["pageid"]}]({page["title"]}) downloaded successfuly ({current} of {amount_wikitext})')
            current = current + 1
            time.sleep(2)
        return current

    def run_text_download(self, amount_text=100):
        current = 1
        pages_text = self.get_pages_for_text_download(amount_text)
        print(f'Running text download for {len(pages_text)} pages')

        for pc in pages_text:
            pageid = pc['pageid']
            text = self.get_text(pageid)
            self.collection_conteudo.update_one(
                { 'pageid': pageid },
                { '$set': { 'text': text['parse']['text'] } }
            )
            self.collection.update_one(
                { 'pageid': pageid },
                { '$set': { 'download_text': 'Done' } }
            )
            print(f'Page text [{pc["pageid"]}]({pc["title"]}) downloaded successfuly ({current} of {amount_text})')
            current = current + 1
            time.sleep(2)

        return current

    def show_text_download_statistics(self):
        pdc = self.get_pages_text_downloads_counts()
        print(f'Page text download counts: {pdc}')

    def show_download_statistics(self):
        pdc = self.get_pages_downloads_counts()
        print(f'Page text download counts: {pdc}')