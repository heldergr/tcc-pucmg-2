import seaborn as sns

class AnaliseGraficaPalavras:

    def __init__(self, informacoes_fonte_de_dados):
        self.__informacoes_fonte_de_dados = informacoes_fonte_de_dados

    """
    Distribuicao de tokens que nao sao verbo nos documentos.
    """
    def analisar_distribuicao_percentual(self, coluna_percentual):
        sns.displot(self.__informacoes_fonte_de_dados, x=coluna_percentual, kind='hist', aspect=1.2)

    """
    Distribuicao de tokens que nao sao verbo nos documentos.
    """
    def analisar_distribuicao_percentual_nao_verbo(self):
        sns.displot(self.__informacoes_fonte_de_dados, x='documento_nao_verbo', kind='hist', aspect=1.2)

    """
    Distribuicao de tokens que nao sao verbos nem stopwords nos documentos.
    """
    def analisar_distribuicao_percentual_nao_stopword(self):
        sns.displot(self.__informacoes_fonte_de_dados, x='documento_nao_verbo_sw', kind='hist', aspect=1.2)

    """
    Distribuicao de tamanhos de documentos diferenciando por conter verbo ou nao.
    """
    def analisar_distribuicao_tamanhos_documentos(self, coluna_tamanho, bidimensional=False, x_max=5000):
        if bidimensional:
            tidy = self.__informacoes_fonte_de_dados[self.__informacoes_fonte_de_dados['tamanho'] <= x_max]
            sns.displot(tidy, x='tamanho', y=coluna_tamanho, kind='hist', aspect=1.2, height=6)
        else:
            tidy = self.__informacoes_fonte_de_dados[['tamanho', coluna_tamanho]].melt().rename(columns={'variable': 'descricao_tamanho' })
            sns.displot(tidy, x='value', kind='hist', aspect=1.2, hue='descricao_tamanho', kde=True, multiple='dodge')

    """
    Distribuicao de tamanhos dos documentos. O parametro indicador_tamanho eh usado para definir se o tamanho eh o original ou 
    o tamanho sem verbo. Possiveis valores: 'tamanho', 'tamanho_sem_verbo'
    """
    def analisar_distribuicao_tamanhos(self, indicador_tamanho='tamanho', x_max=5000):
        limitado = self.__informacoes_fonte_de_dados[self.__informacoes_fonte_de_dados[indicador_tamanho] <= x_max]
        sns.displot(limitado, x=indicador_tamanho, kind='hist', aspect=1.2)