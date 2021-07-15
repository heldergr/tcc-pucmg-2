import pandas as pd

class FonteDados:

    def __init__(self, carregar_previamente=False):
        if carregar_previamente:
            self.carregar_dados()
        self.__df = None

    def carregar_dados(self, limpar_stopwords_especificas=True):
        pass

    def get_dataframe(self):
        return pd.DataFrame({'tokens': [], 'n_tokens': []})

    def get_conteudo_original(self):
        return None

    def get_tokens(self):
        return self.get_dataframe()['tokens']

    def get_ntokens(self):
        return self.get_dataframe()['n_tokens']
