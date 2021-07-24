from fonte_dados.fabrica import FabricaFonteDados
from treinamento.treinamento_lda import TreinamentoLda
from util import constants

def treinar_modelo(fonte_origem, num_topics, limpar_stopwords_especificas=False, limpar_verbos=False):
    fabrica = FabricaFonteDados()

    # Carregar fonte de dados de origem
    fonte_dados_origem = fabrica.get_fonte_dados(fonte_origem)
    fonte_dados_origem.carregar_dados(limpar_stopwords_especificas=limpar_stopwords_especificas, limpar_verbos=limpar_verbos)
    documentos_origem = fonte_dados_origem.get_tokens()

    # Ajuste de modelo
    treinamento_lda = TreinamentoLda(num_topics=num_topics, passes=2)
    resultado_lda = treinamento_lda.ajustar_modelo(documentos_origem)
    lda = resultado_lda.modelo_lda
    return lda


# Fonte NERDS_VIAJANTES, 57 tópicos, sem limpeza de stopwords específicas, sem limpeza de verbos
lda_inicial = treinar_modelo(fonte_origem=constants.NERDS_VIAJANTES, num_topics=57)

# Fonte NERDS_VIAJANTES, 57 tópicos, com limpeza de stopwords específicas, sem limpeza de verbos
lda_limpeza_stopwords_especificas = treinar_modelo(fonte_origem=constants.NERDS_VIAJANTES, num_topics=57, limpar_stopwords_especificas=True)

# Fonte NERDS_VIAJANTES, 57 tópicos, com limpeza de stopwords específicas, com limpeza de verbos
lda_limpeza_verbos = treinar_modelo(fonte_origem=constants.NERDS_VIAJANTES, num_topics=57, limpar_stopwords_especificas=True, limpar_verbos=True)