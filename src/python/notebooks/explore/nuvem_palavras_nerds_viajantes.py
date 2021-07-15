import matplotlib.pyplot as plt
from wordcloud import WordCloud

class AnaliseNuvemPalavras:

    def __init__(self, informacoes_fonte_de_dados):
        self.__informacoes_fonte_de_dados = informacoes_fonte_de_dados

    def __obter_texto_unico(self, coluna_documento):
        corpus = list(self.__informacoes_fonte_de_dados[coluna_documento].values)
        corpus = [" ".join(documento) for documento in corpus]
        textao = " ".join(corpus)
        return textao

    def gerar_nuvem_palavras(self, coluna_documento):
        texto_unico = self.__obter_texto_unico(coluna_documento)
        wordcloud = WordCloud(background_color='white').generate(texto_unico)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()