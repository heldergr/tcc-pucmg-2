from limpeza.wikipedia import WikipediaCleaner

import pandas as pd
from bs4 import BeautifulSoup

class WikipediaExplorer:

    def __init__(self, wikipedia_repo):
        self.wikipedia_repo = wikipedia_repo

    def create_dataframe(self):
        pages = self.wikipedia_repo.find_all()
        return pd.DataFrame(pages)

    def show_pages_count(self, pages_df):
        print(f'Foram encontradas {len(pages_df)} páginas com contéudo')

    def explore(self):
        print('Running wikipedia explorer...')
        pages_df = self.create_dataframe()
        pages_df = pages_df.drop(['_id', 'ns', 'type', 'download', 'categories', 'wikitext'], axis='columns')
        self.show_pages_count(pages_df)

        wikipedia_cleaner = WikipediaCleaner()
        # pages_df['text_processed'] =  wikipedia_cleaner.

    def extract_text(self, raw_text):
        soup = BeautifulSoup(raw_text, 'html.parser')
        ps = soup.find_all('p')
        pres = soup.find_all('pre')

        ps_text = ' '.join([p.getText() for p in ps])
        pres_text = ' '.join([pre.getText() for pre in pres])

        return (ps_text, pres_text)