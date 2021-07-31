from scipy.spatial import distance
import numpy as np

class SimilarityCalculator:

    def __init__(self, matriz_esparsa_alvo) -> None:
        self.__matriz_esparsa_alvo = matriz_esparsa_alvo

    def get_matriz_esparsa_alvo(self):
        return self.__matriz_esparsa_alvo

    """
    Params: probabilidades_documento: Probabilides do documento para o qual se deseja calcular a distancia
    """
    def jensen_shannon2(self, probabilidades_documento):
        sim = [distance.jensenshannon(data, probabilidades_documento) for data in self.__matriz_esparsa_alvo]
        return np.array(sim)

    """
    This function implements the Jensen-Shannon distance above
    and retruns the top k indices of the smallest jensen shannon distances
    between one document and all document probabilities in the sparse matrix
    """
    def get_most_similar_documents(self, probabilidades_documento, k=10, return_distances=False):
        # Calcula lista de distancias jensen shannon
        sims = self.jensen_shannon2(probabilidades_documento)

        # Ordena para obter os documentos mais proximos de acordo com a distancia Jensen Shannon
        most_similar = sims.argsort()[:k]

        if return_distances:
            return (most_similar, sims[most_similar])
        else:
            return most_similar