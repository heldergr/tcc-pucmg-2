import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
from pymongo import MongoClient
import nltk

url_base = 'https://www.conjugacao.com.br/verbos-populares'

stemmer = nltk.stem.RSLPStemmer()

class VerbosCollector:

    def __init__(self, collection_name = 'verbos'):
        self.__collection_name = collection_name

    def get_verbos_pagina(self, url_pagina):
        print(f'Buscando verbos da pagina {url_pagina}')
        # Espera 5 segundos antes de buscar a proxima pagina
        time.sleep(5)
        page = requests.get(url_pagina)
        if page.status_code == 200:
            soap = BeautifulSoup(page.text, 'html.parser')
            div_content = soap.find('div', {'id': 'content'})
            lis = div_content.findChildren('li')
            verbos_pagina = [li.getText() for li in lis]
            return verbos_pagina
        else:
            return []

    def __get_collection_verbos(self):
        client = MongoClient()
        tcc_pucmg_db = client['tcc-pucmg']
        return tcc_pucmg_db[self.__collection_name]

    def __criar_documento(self, verbo):
        return {
            'verbo': verbo,
            'verbo_stemmed': stemmer.stem(verbo)
        }

    def collect(self):
        urls_paginas = [url_base] + [f'{url_base}/{i}/' for i in range(2, 51)]
        verbos_por_paginas = [self.get_verbos_pagina(url) for url in urls_paginas]
        todos_verbos = [verbo for verbos_pagina in verbos_por_paginas for verbo in verbos_pagina]
        verbos = self.__get_collection_verbos()
        documentos_verbos = [self.__criar_documento(v) for v in todos_verbos]
        verbos.insert_many(documentos_verbos)
