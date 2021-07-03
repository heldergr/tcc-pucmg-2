from scipy.spatial import distance
import numpy as np

class SimilarityCalculator:

    def __init__(self, resultado_treinamento_lda):
        self.resultado_treinamento_lda = resultado_treinamento_lda
        self.modelo_lda = self.resultado_treinamento_lda.modelo_lda
        self.corpus = self.resultado_treinamento_lda.corpus
        
        # Cria matrix sparse para ser usada no calculo da distancia entre os documentos com base nas probabilidades de seus topicos
        self.__sparse_matrix = self.__create_sparse_matrix()

    def __create_sparse_matrix(self):
        doc_topic_dist = np.array([[tup[1] for tup in lst] for lst in self.modelo_lda[self.corpus]])
        return doc_topic_dist

    """
    Params: 
    query: Probabilides do documento para o qual se deseja calcular a distancia
    """
    def jensen_shannon2(self, probabilidades_documentos):
        sim = [distance.jensenshannon(data, probabilidades_documentos) for data in self.__sparse_matrix]
        return np.array(sim)

    """
    This function implements the Jensen-Shannon distance above
    and retruns the top k indices of the smallest jensen shannon distances
    """
    def get_most_similar_documents(self, probabilidades_documentos, k=10):
        # Calcula lista de distancias jensen shannon
        sims = self.jensen_shannon2(probabilidades_documentos)

        # Ordena para obter os documentos mais proximos de acordo com a distancia Jensen Shannon
        return sims.argsort()[:k] 