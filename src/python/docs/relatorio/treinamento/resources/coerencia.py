from gensim.corpora import Dictionary
from gensim.models import LdaModel, CoherenceModel

import pandas as pd
import time

class CalculadorCoerencia:

    def __init__(self, fonte_dados_origem):
        self.__documentos = fonte_dados_origem.get_tokens()

    def calcular_coerencia(self, num_topics, corpus, id2word):
        """Compute coherence score given a number of topics."""
        lda = LdaModel(corpus=corpus, id2word=id2word, num_topics=num_topics,
            passes=20, random_state=0)
        cm = CoherenceModel(model=lda, texts=self.__documentos, dictionary=id2word, coherence='c_v')
        return cm.get_coherence()

    def calcular_coerencias(self, topicos_inicio, topicos_fim, debug=False):
        id2word = Dictionary(self.__documentos)
        corpus = [id2word.doc2bow(documento) for documento in self.__documentos]

        coherence = pd.DataFrame(index=range(topicos_inicio, topicos_fim + 1), 
            columns=['coherence', 'tempo_gasto'])

        for i in coherence.index:
            if debug:
                print(f'Calculando coerencia para {i} topicos...')
            tempo_antes = time.time()
            c = self.calcular_coerencia(i, corpus, id2word)
            tempo_depois = time.time()
            coherence.loc[i, 'coherence'] = c
            coherence.loc[i, 'tempo_gasto'] = tempo_depois - tempo_antes

        return coherence
