from nltk import word_tokenize
from nltk.stem import RSLPStemmer
from nltk.corpus import stopwords

def clean_melhores_destinos(md_posts):
    # Converte conteudo para lowercase
    md_posts['Texto_clean'] = md_posts['Texto'].apply(lambda x: x.lower())
    
    # Quebra os posts em tokens
    md_posts['Texto_tokens'] = md_posts['Texto_clean'].apply(lambda x: word_tokenize(x))

    # Remove stopwords em portuges
    pt_stop = stopwords.words('portuguese')
    md_posts['Texto_tokens'] = md_posts['Texto_tokens'].apply(lambda xs: [x for x in xs if x not in pt_stop])

    stemmer = RSLPStemmer()
    md_posts['Texto_stem'] = md_posts['Texto_tokens'].apply(lambda x: [stemmer.stem(y) for y in x])

    return md_posts

if __name__ == "__main__":
    print("Imported worked fine")