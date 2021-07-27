from limpeza.limpeza_texto import remover_html_tags
from repository.mongo_utils import get_wikipedia_collection, get_pages_content_collection
from repository.wikipedia import WikipediaRepo

import time
from bs4 import BeautifulSoup

class WikipediaCleaner:

    def __init__(self):
        pass

    def clean_text(self, content, html=True):
        processed = content
        if html:
            processed = remover_html_tags(content)
        return processed

    def extrair_texto_puro(self, raw_text):
        soup = BeautifulSoup(raw_text, 'html.parser')
        ps = soup.find_all('p')
        pres = soup.find_all('pre')

        ps_text = ' '.join([p.getText() for p in ps])
        pres_text = ' '.join([pre.getText() for pre in pres])

        return ps_text + ' ' + pres_text

    """
    Metodo que faz a extracao do texto puro a partir do html completo que foi feito download via API da Wikipedia.
    O conteudo apos esta extracao nao contem tags html e estas nao precisam ser removidas em tratamento posterior.

    Eh um pouco mais demorado porque extrai os textos de todas as paginas. Em geral demora entre 30 e 40 segundos para execucao total.
    """
    def extrair_textos_puros(self, collection_name: None):
        print('Inicio da extracao de texto puro...')
        start_time = time.time()
        pages_content = None
        if collection_name is not None:
            pages_content = get_wikipedia_collection(collection_name=collection_name)
        else:
            pages_content = get_pages_content_collection()
        wikipedia_repo = WikipediaRepo(collection=pages_content)
        pages = wikipedia_repo.find_all()
        print(f'Extracao sera feita para {len(pages)} paginas')

        for page in pages:
            print(f'Extraindo texto puro para {page["title"]}')
            texto_puro = self.extrair_texto_puro(page['text'])
            wikipedia_repo.set_text_clean(page['_id'], texto_puro)

        print('Fim da extracao de texto puro...')
        print(f'Tempo gasto na extracao: {(time.time() - start_time)} segundos')
        
