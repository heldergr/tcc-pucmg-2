from fonte_dados.fabrica import FabricaFonteDados
from similarity.similarity import SimilarityCalculator
from treinamento.treinamento_lda import TreinamentoLda

import pandas as pd

fabrica = FabricaFonteDados()

def executar_treinamento(id_cenario, fonte_origem, fonte_destino, num_topics):
    print("Carregando dados de origem...")
    fonte_dados_origem = fabrica.get_fonte_dados(fonte_origem)
    fonte_dados_origem.carregar_dados()
    documentos_origem = fonte_dados_origem.get_tokens()

    # Ajusta modelo LDA para os documentos de origem. O resultado gerado contem o dicionario, o corpus de dados e o modelo gerado
    print("Ajustando modelo para dados de origem...")
    treinamento_lda = TreinamentoLda(num_topics=num_topics, passes=2)
    resultado_lda = treinamento_lda.ajustar_modelo(documentos_origem)

    print("Calculando probabilidades para topicos de origem...")
    probabilidades_topicos_origem = [treinamento_lda.calcular_probabilidades_documento(dnv, resultado_lda) for dnv in documentos_origem]

    print("Carregando dados de destino...")
    fonte_dados_destino = fabrica.get_fonte_dados(fonte_destino)
    fonte_dados_destino.carregar_dados()
    documentos_destino = fonte_dados_destino.get_tokens()

    print("Calculando probabilidades para topicos de destino...")
    probabilidades_topicos_destino = [
        treinamento_lda.calcular_probabilidades_documento(dw, resultado_lda) for dw in documentos_destino]

    print("Executando calculo de similaridade entre documentos...")
    similarity_calculator = SimilarityCalculator(probabilidades_topicos_destino)

    print("Calculando documentos mais parecidos...")
    destinos_mais_parecidos = [similarity_calculator.get_most_similar_documents(pto, return_distances=True) for pto in probabilidades_topicos_origem]
    
    destino_mais_parecido = [dmp[0][0] for dmp in destinos_mais_parecidos]
    distancia_mais_parecido = [dmp[1][0] for dmp in destinos_mais_parecidos]

    print("Montando resultado...")
    destino_df = fonte_dados_destino.get_dataframe()

    titulos_destino = destino_df['titulo'].values
    titulos_mais_parecidos = [titulos_destino[dmp] for dmp in destino_mais_parecido]

    ids_documentos_destino = destino_df['id_documento'].values
    ids_documentos_mais_parecidos = [ids_documentos_destino[dmp] for dmp in destino_mais_parecido]

    resultado_df = pd.DataFrame(data = {
        'id_documento_origem': fonte_dados_origem.get_dataframe()['id_documento'].values,
        'titulo_documento_origem': fonte_dados_origem.get_dataframe()['titulo'].values,
        'id_documento_destino': ids_documentos_mais_parecidos,
        'titulo_documento_destino': titulos_mais_parecidos,
        'distancia_destino': distancia_mais_parecido,
        'id_cenario': id_cenario,
        'fonte_origem': fonte_origem,
        'fonte_destino': fonte_destino
    })

    return resultado_df

class ExecutorTreinamento():

    def __init__(self, id_cenario, fonte_origem, fonte_destino, num_topics):
        self.__id_cenario = id_cenario
        self.__fonte_origem = fonte_origem
        self.__fonte_destino = fonte_destino
        self.__num_topics = num_topics

    def executar_treinamento(self):
        fonte_dados_origem = fabrica.get_fonte_dados(self.__fonte_origem)
        fonte_dados_origem.carregar_dados()
        documentos_origem = fonte_dados_origem.get_tokens()

        # Ajusta modelo LDA para os documentos de origem. O resultado gerado contem o dicionario, o corpus de dados e o modelo gerado
        treinamento_lda = TreinamentoLda(num_topics=self.__num_topics, passes=2)
        resultado_lda = treinamento_lda.ajustar_modelo(documentos_origem)

        probabilidades_topicos_origem = [treinamento_lda.calcular_probabilidades_documento(dnv, resultado_lda) for dnv in documentos_origem]

        fonte_dados_destino = fabrica.get_fonte_dados(self.__fonte_destino)
        fonte_dados_destino.carregar_dados()
        documentos_destino = fonte_dados_destino.get_tokens()

        probabilidades_topicos_destino = [
            treinamento_lda.calcular_probabilidades_documento(dw, resultado_lda) for dw in documentos_destino]

        similarity_calculator = SimilarityCalculator(probabilidades_topicos_destino)

        destinos_mais_parecidos = [similarity_calculator.get_most_similar_documents(pto, return_distances=True) for pto in probabilidades_topicos_origem]
        
        destino_mais_parecido = [dmp[0][0] for dmp in destinos_mais_parecidos]
        distancia_mais_parecido = [dmp[1][0] for dmp in destinos_mais_parecidos]

        destino_df = fonte_dados_destino.get_dataframe()

        titulos_destino = destino_df['titulo'].values
        titulos_mais_parecidos = [titulos_destino[dmp] for dmp in destino_mais_parecido]

        ids_documentos_destino = destino_df['id_documento'].values
        ids_documentos_mais_parecidos = [ids_documentos_destino[dmp] for dmp in destino_mais_parecido]

        resultado_df = pd.DataFrame(data = {
            'id_documento_origem': fonte_dados_origem.get_dataframe()['id_documento'].values,
            'titulo_documento_origem': fonte_dados_origem.get_dataframe()['titulo'].values,
            'id_documento_destino': ids_documentos_mais_parecidos,
            'titulo_documento_destino': titulos_mais_parecidos,
            'distancia_destino': distancia_mais_parecido,
            'id_cenario': self.__id_cenario,
            'fonte_origem': self.__fonte_origem,
            'fonte_destino': self.__fonte_destino
        })

        return resultado_df