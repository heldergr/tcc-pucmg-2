from repository.verbos import VerbosRepo

import pandas as pd

verbos_repo = VerbosRepo()

class FonteDados:

    def __init__(self, carregar_previamente=False):
        if carregar_previamente:
            self.carregar_dados()
        self.__df = None

    def carregar_dados(self, limpar_stopwords_especificas=True, limpar_verbos=True):
        pass

    def get_dataframe(self):
        return pd.DataFrame({'tokens': [], 'n_tokens': []})

    def get_conteudo_original(self):
        return None

    def get_tokens(self):
        return self.get_dataframe()['tokens']

    def get_ntokens(self):
        return self.get_dataframe()['n_tokens']

    """
    Remove verbos da lista de tokens
    """
    def remover_verbos(self, tokens):
        todos_verbos = verbos_repo.find_all_stemmed()
        tokens_sem_verbos = [token for token in tokens if token not in todos_verbos]
        print(f'Tamanho com verbos: {len(tokens)}, tamanho sem verbos: {len(tokens_sem_verbos)}')
        return tokens_sem_verbos

