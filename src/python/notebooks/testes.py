from explore.estatistica_palavras import AnaliseEstatisticaPalavras
from explore.informacoes_fontes_dados import obter_informacoes_palavras
from explore.wikipedia import WikipediaExplorer
from repository.wikipedia import WikipediaRepo
from repository.mongo_utils import get_pages_content_collection
from limpeza.wikipedia import WikipediaCleaner
from limpeza.stopwords_especificas import StopwordsSpecificas
from util import constants

def executar_extracao_textos_puros():
    wikipedia_cleaner = WikipediaCleaner()
    wikipedia_cleaner.extrair_textos_puros()

def executar_carregar_stopwords_especificas():
    stopwords_especificas = StopwordsSpecificas()
    palavras_especificas = stopwords_especificas.carregar_palavras_especificas(constants.NERDS_VIAJANTES)
    print(palavras_especificas)

def executar_analise_estatisticas_palavras():
    pass

def executar_informacoes_fontes_dados():
    informacoes_fonte_de_dados = obter_informacoes_palavras(constants.NERDS_VIAJANTES)
    print(informacoes_fonte_de_dados)

def executar_estatistica_palavras():
    informacoes_fonte_de_dados = obter_informacoes_palavras(constants.NERDS_VIAJANTES)
    analise_estatistica = AnaliseEstatisticaPalavras(informacoes_fonte_de_dados)
    analise_estatistica.exibir_total_tokens('documento')

if __name__ == '__main__':

    executar_estatistica_palavras()

    run_all = False

    if run_all:
        executar_informacoes_fontes_dados()
        executar_carregar_stopwords_especificas()
        wikipedia_repo = WikipediaRepo(collection=get_pages_content_collection())
        wikipedia_explorer = WikipediaExplorer(wikipedia_repo)
        wikipedia_explorer.explore()
        executar_extracao_textos_puros()
