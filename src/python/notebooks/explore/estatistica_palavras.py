from collections import Counter

class AnaliseEstatisticaPalavras:

    def __init__(self, informacoes_fonte_de_dados):
        self.__informacoes_fonte_de_dados = informacoes_fonte_de_dados

    def __obter_todos_tokens(self, coluna_documento):
        documentos = list(self.__informacoes_fonte_de_dados[coluna_documento].values)
        return [token for documento in documentos for token in documento]

    """
    Exibicao de total geral dos tokens da coluna de documentos selecionada
    """
    def exibir_total_tokens(self, coluna_documento):
        todos_tokens = self.__obter_todos_tokens(coluna_documento)
        print(f'O total de tokens de todos os documentos para a coluna "{coluna_documento}" eh {len(todos_tokens)}')

    """
    Exibicao de top n tokens mais comuns, ordenados do mais frequente para o menos frequente
    """
    def exibir_tokens_mais_comuns(self, coluna_documento, n=10):
        todos_tokens = self.__obter_todos_tokens(coluna_documento)
        print(Counter(todos_tokens).most_common(n))

    """
    Descricao estatistica dos tamanhos dos documentos no corpo. Exibe diversas informacoes estatisticas, como media, desvio padra, etc,
    alem dos percentiles selecionados
    """
    def analisar_tamanhos_documentos(self):
        print(self.__informacoes_fonte_de_dados[['tamanho', 'tamanho_sem_verbo', 'tamanho_sem_verbo_sw']].describe(percentiles=[.05, .1, .25, .5, .75, .9, .95]))
