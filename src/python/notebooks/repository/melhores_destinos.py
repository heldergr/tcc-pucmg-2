from bs4 import BeautifulSoup
import pandas as pd

def carregar_conteudo(filename):
    with open(filename, encoding='utf-8') as f:
        data = f.read()
        return data

def get_promocoes(filename = '/Users/heldergeraldoribeiro/Documents/estudos/data-science/tcc-pucmg/data/melhores_destinos/index.html'):
    # Faz parte do conteudo usando o BeautifulSoup
    content = carregar_conteudo(filename)
    soup = BeautifulSoup(content, 'html.parser')

    # Carrega titulos e resumos dos posts
    articles = soup.find_all('div', { "class":  "post-promo-home-c2"})

    aa = [(a.findChild('a').get('title'), a.getText()) for a in articles]

    md_posts = pd.DataFrame(aa, columns = ['Titulo', 'Texto'])
    return md_posts

if __name__ == "__main__":
    print("5 primeiros posts do melhores destinos:\n")
    melhores_destinos = get_promocoes()
    print(melhores_destinos.head())