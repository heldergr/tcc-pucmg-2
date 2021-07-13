from fonte_dados.fabrica import FabricaFonteDados, NERDS_VIAJANTES
from treinamento.treinamento_lda import TreinamentoLda
from repository.mongo_utils import get_pages_content_collection
from repository.wikipedia import WikipediaRepo

wikipedia_repo = WikipediaRepo(collection=get_pages_content_collection())
fabrica = FabricaFonteDados()

origem = NERDS_VIAJANTES

# Carregando fonte de dados de origem
fonte_dados_origem = fabrica.get_fonte_dados(origem)
fonte_dados_origem.carregar_dados()
documentos_origem = fonte_dados_origem.get_tokens()

# Ajuste de modelo para base de treinamento de origem
treinamento_lda = TreinamentoLda(num_topics=100, passes=2)
resultado_lda = treinamento_lda.ajustar_modelo(documentos_origem)
lda = resultado_lda.modelo_lda

# Analise de topicos
lda.show_topics(num_topics=10, num_words=5)