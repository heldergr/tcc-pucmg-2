import pandas as pd

from gensim.corpora import Dictionary
from gensim.models import LdaModel, CoherenceModel

def ajustar_modelo(documentos, num_topics = 5):
    # Creates a dictionary, mapping words to ids
    id2word = Dictionary(documentos)

    # Mapeamento de id para palavras
    # id2word.token2id
    # We can see word: word id pairs in this output.

    # Cria corpus com base nos documentos e no mapeamento de id para palavra
    # Para cada documento faz a contagem de vezes que um determinado topico
    # aparece no documento
    corpus = [id2word.doc2bow(documento) for documento in documentos]

    # print(corpus[0])
    
    lda = LdaModel(corpus=corpus, id2word=id2word, 
               num_topics=num_topics, passes=20, 
               random_state=0)

    return lda

def calcular_coerencia(num_topics, corpus, id2word, documentos):
    """Compute coherence score given a number of topics."""
    lda = LdaModel(corpus=corpus, id2word=id2word, num_topics=num_topics,
        passes=20, random_state=0)
    cm = CoherenceModel(model=lda, texts=documentos, dictionary=id2word, coherence='c_v')
    return cm.get_coherence()

def calcular_coerencias(documentos, topicos_inicio, topicos_fim):
    id2word = Dictionary(documentos)
    corpus = [id2word.doc2bow(documento) for documento in documentos]

    coherence = pd.DataFrame(index=range(topicos_inicio, topicos_fim + 1), 
        columns=['coherence'])

    for i in coherence.index:
        c = calcular_coerencia(i, corpus, id2word, documentos)
        coherence.loc[i, 'coherence'] = c

    return coherence

def imprimir_topicos(lda_model, num_topics):
    for i in range(num_topics):
        print(f"********** Topic {i+1} **********")
        print(lda_model.print_topic(i), '\n')

# Adiciona probabilidades que um documento tenham os topicos
# definidos para um modelo.

# Metodo espera um documento que ja venha divido em tokens
def calcular_probabilidades(documento, id2word, lda_model):
    """Add probabilities for topics for a document."""
    corpus = id2word.doc2bow(documento)

    # Predict probabilities
    predictions = lda_model.get_document_topics(corpus, minimum_probability=0.0)
    topics = [topic for topic, probability in predictions]
    return [prediction[1] for prediction in predictions]

