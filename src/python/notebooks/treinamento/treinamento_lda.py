import treinamento.dicionario as dicionario

import pandas as pd

from gensim.corpora import Dictionary
from gensim.models import LdaModel, CoherenceModel

class ResultadoTreinamentoLda:

    def __init__(self, dicionario, corpus, modelo_lda):
        self.dicionario = dicionario
        self.corpus = corpus
        self.modelo_lda = modelo_lda

class TreinamentoLda:

    def __init__(self, num_topics = 13, passes = 20):
        self.num_topics = num_topics
        self.passes = passes

    def ajustar_modelo(self, documentos, alpha=1e-2, eta=0.5e-2):
        # Cria dicionario
        id2word = dicionario.criar(documentos)

        # Cria corpus com base nos documentos e no mapeamento de id para palavra
        # Para cada documento faz a contagem de vezes que um determinado topico
        # aparece no documento
        corpus = [id2word.doc2bow(documento) for documento in documentos]

        print(f'Ajustando modelo com {self.num_topics} topicos e {self.passes} passes')

        # Treina modelo LDA        
        lda = LdaModel(corpus=corpus, id2word=id2word, 
                num_topics=self.num_topics, passes=self.passes, 
                alpha=alpha, eta=eta,
                random_state=0)

        return ResultadoTreinamentoLda(id2word, corpus, lda)

    """
    Adiciona probabilidades que um documento tenham os topicos definidos para um modelo.

    Calcula probabilidades que um determinado documento tenha os topicos encontrados em um modelo lda.
    Metodo espera um documento que ja venha divido em tokens.
    """
    def calcular_probabilidades_documento(self, documento, resultado_treinamento_lda):
        """Add probabilities for topics for a document."""
        corpus = resultado_treinamento_lda.dicionario.doc2bow(documento)

        # Predict probabilities
        predictions = resultado_treinamento_lda.modelo_lda.get_document_topics(corpus, minimum_probability=0.0)
        topics = [topic for topic, probability in predictions]
        return [prediction[1] for prediction in predictions]


def ajustar_modelo(documentos, id2word, num_topics = 13):
    # Cria corpus com base nos documentos e no mapeamento de id para palavra
    # Para cada documento faz a contagem de vezes que um determinado topico
    # aparece no documento
    corpus = [id2word.doc2bow(documento) for documento in documentos]
    
    lda = LdaModel(corpus=corpus, id2word=id2word, 
               num_topics=num_topics, passes=20, 
               random_state=0)

    return ResultadoTreinamentoLda(id2word, corpus, lda)

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