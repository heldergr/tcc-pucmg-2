import nltk
import re

"""
A list of stopwords can be found in the corpus module of nltk package. We are going to try to use the portuguese version. The download code is necessary only once.
"""
from nltk.corpus import stopwords

# import nltk
# nltk.download('stopwords')

pt_stopwords = stopwords.words('portuguese')
stemmer = nltk.stem.RSLPStemmer()

from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer

def remover_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def remover_pontuacoes(text):
    # tokeniser = RegexpTokenizer(r'[A-Za-z]{3,}')

    """
    Tentativa de resolver problema de palavras com acento

    Possibilidades:
    - Adicionar lista de letras com acento
    - Usar \w+ para pegar todas as palavas

    Ideia adotada pelo presente momento:
    - Usar \w+ para pegar todas as palavas
    """
    # tokeniser = RegexpTokenizer(r'[A-Za-z]{3,}')
    tokeniser = RegexpTokenizer(r'\w{3,}')

    tokens = tokeniser.tokenize(text)
    return ' '.join(tokens)

def remove_stopwords(tokens):
    return [word for word in tokens if not word in pt_stopwords]

def stemm_text(tokens):
    return [stemmer.stem(token) for token in tokens]

"""
Remover caption de imagens
"""
def remover_caption(text):
    clean = re.compile('\[.*caption.*\]')
    return re.sub(clean, '', text)

# Verificar se este tratamento ficara aqui ou no notebook
def preprocess_content(content):
    result = content.apply(lambda x: limpar_texto(x))
    return result

def limpar_texto(texto, limpar_stopwords = True, stemming = True):
    texto = remover_html_tags(texto)
    texto = remover_caption(texto)
    texto = remover_pontuacoes(texto)

    tokens = word_tokenize(texto)

    if limpar_stopwords:
        tokens = remove_stopwords(tokens)

    if stemming:
        tokens = stemm_text(tokens)

    return tokens

if __name__ == '__main__':
    print('Modulo de limpeza de texto...')
    print(limpar_texto('Meu nome. eh Hélder, Ribeiro!'))
    print(limpar_texto('Meu nome. eh Helder, Ribeiro!'))