from limpeza.limpeza_texto import remover_html_tags

from bs4 import BeautifulSoup

class WikipediaCleaner:

    def __init__(self):
        pass

    def clean_text(self, content, html=True):
        processed = content
        if html:
            processed = remover_html_tags(content)
        return processed