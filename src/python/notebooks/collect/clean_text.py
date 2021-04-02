import nltk
import re

"""
A list of stopwords can be found in the corpus module of nltk package. We are going to try to use the portuguese version. The download code is necessary only once.
"""
from nltk.corpus import stopwords

# import nltk
# nltk.download('stopwords')

from nltk.tokenize import word_tokenize

def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def remove_stopwords(text, pt_stopwords):
    text_tokens = word_tokenize(text)
    tokens_without_sw = [word for word in text_tokens if not word in pt_stopwords]
    return " ".join(tokens_without_sw)

def stemm_text(text, stemmer):
    tokens = word_tokenize(text)
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return " ".join(stemmed_tokens)

def preprocess_text(text, pt_stopwords, stemmer):
    no_html = remove_html_tags(text)
    no_sw = remove_stopwords(text, pt_stopwords)
    stemmed = stemm_text(no_sw, stemmer)
    preprocessed = stemmed
    return preprocessed

def preprocess_content(content):
    pt_stopwords = stopwords.words('portuguese')
    stemmer = nltk.stem.RSLPStemmer()
    result = content.apply(lambda x: preprocess_text(x, pt_stopwords, stemmer))
    return result