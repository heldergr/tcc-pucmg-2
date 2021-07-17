from fonte_dados.fonte_dados import FonteDados
from limpeza import limpeza_texto
from repository.mongo_utils import get_pages_content_collection
from repository.wikipedia import WikipediaRepo

import pandas as pd

wikipedia_repo = WikipediaRepo(collection=get_pages_content_collection())

class Wikipedia(FonteDados):

    def __init__(self, carregar_previamente=True):
        super().__init__(carregar_previamente=carregar_previamente)
        self.__pages = None

    def carregar_dados(self, limpar_stopwords_especificas=True, limpar_verbos=True):
        pages = wikipedia_repo.find_all()
        self.__pages = pages

        pages_df = pd.DataFrame(pages)
        pages_df = pages_df.drop(['_id', 'ns', 'type', 'download', 'categories', 'wikitext', 'text'], axis='columns')

        # Limpa texto e gera documentos para treinamento
        tokens = pages_df['text_clean'].apply(limpeza_texto.limpar_texto)

        if limpar_verbos:
            tokens = [self.remover_verbos(tokens_documento) for tokens_documento in tokens]

        pages_df['tokens'] = tokens
        n_tokens = [len(tks) for tks in tokens]
        pages_df['n_tokens'] = n_tokens


        pages_df.rename(columns={'text_clean': 'documento', 'pageid': 'id_documento', 'title': 'titulo'}, inplace=True)
        pages_df['nome'] = pages_df['titulo']

        self.__pages_df = pages_df

    """
    Colunas esperadas no dataframe de retorno:
    - id_documento: id do documento na fonte de dados
    - nome: nome do documento na fonte de dados
    - titulo: titulo descritivo do documento na fonte de dados
    - documento: conteudo original do documento
    - n_characters: tamanho do documento em caracteres
    - tokens: tokens do documento apos limpeza
    - n_tokens: tamanho do documento em tokens
    """
    def get_dataframe(self):
        return self.__pages_df

    def get_conteudo_original(self):
        return self.__pages