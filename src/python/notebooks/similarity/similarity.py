from scipy.spatial import distance
import numpy as np

class SimilarityCalculator:

    # def __init__(self, resultado_treinamento_lda, num_topics):
    #     self.resultado_treinamento_lda = resultado_treinamento_lda
    #     self.modelo_lda = self.resultado_treinamento_lda.modelo_lda
    #     self.corpus = self.resultado_treinamento_lda.corpus
    #     self.num_topics = num_topics
        
    #     # Cria matrix sparse para ser usada no calculo da distancia entre os documentos com base nas probabilidades de seus topicos
    #     self.__sparse_matrix = self.__create_sparse_matrix()

    def __init__(self, matriz_esparsa_alvo) -> None:
        self.__matriz_esparsa_alvo = matriz_esparsa_alvo

    # def fill_topic_probabilities(self, topics_probabilities):
    #     full_probabilities = np.repeat(0.0, self.num_topics)
    #     for tup in topics_probabilities:
    #         full_probabilities[tup[0]] = tup[1]

    #     return full_probabilities

    # def __create_sparse_matrix(self):
    #     # doc_topic_dist = np.array([[tup[1] for tup in lst] for lst in self.modelo_lda[self.corpus]])
    #     doc_topic_dist = np.array([self.fill_topic_probabilities(lst) for lst in self.modelo_lda[self.corpus]])
    #     return doc_topic_dist

    def get_matriz_esparsa_alvo(self):
        return self.__matriz_esparsa_alvo

    """
    Params: 
    query: Probabilides do documento para o qual se deseja calcular a distancia
    """
    def jensen_shannon2(self, probabilidades_documento):
        sim = [distance.jensenshannon(data, probabilidades_documento) for data in self.__matriz_esparsa_alvo]
        return np.array(sim)

    """
    This function implements the Jensen-Shannon distance above
    and retruns the top k indices of the smallest jensen shannon distances
    between one document and all document probabilities in the sparse matrix
    """
    def get_most_similar_documents(self, probabilidades_documento, k=10):
        # Calcula lista de distancias jensen shannon
        sims = self.jensen_shannon2(probabilidades_documento)

        # Ordena para obter os documentos mais proximos de acordo com a distancia Jensen Shannon
        return sims.argsort()[:k] 