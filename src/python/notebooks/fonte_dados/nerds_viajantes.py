from fonte_dados.fonte_dados import FonteDados
from limpeza import limpeza_posts, limpeza_texto
from repository import nerds_viajantes as nerds_viajantes_repo

class NerdsViajantes(FonteDados):

    def __init__(self, carregar_previamente=True):
        super().__init__(carregar_previamente=carregar_previamente)
        self.__posts = None

    def __remover_propaganda_hoteis(self, texto):
        inicio_propaganda_hoteis = '________________________________________________________'
        if texto.count(inicio_propaganda_hoteis) > 0:
            indice_propaganda_hoteis = texto.index(inicio_propaganda_hoteis)
            return texto[:indice_propaganda_hoteis]
        else:
            return texto

    def __limpar_texto(self, texto):
        texto_limpo = limpeza_texto.limpar_texto(texto)
        texto_limpo = self.__remover_propaganda_hoteis(texto_limpo)
        return texto_limpo

    def carregar_dados(self):
        self.__published = nerds_viajantes_repo.read_published()
        
        # Remove posts desnecessarios
        posts = limpeza_posts.limpar_posts(self.__published)
        posts.reset_index(inplace=True)

        posts.rename(columns={'content': 'documento', 'id': 'id_documento', 'name': 'nome', 'title': 'titulo'}, inplace=True)

        # Limpa texto e gera documentos para treinamento
        # tokens = posts['documento'].apply(limpeza_texto.limpar_texto)
        tokens = posts['documento'].apply(self.__limpar_texto)
        posts['tokens'] = tokens
        n_tokens = [len(tks) for tks in tokens]
        posts['n_tokens'] = n_tokens

        # Remove colunas desnecessarias
        posts.drop(columns=['index', 'date', 'modified', 'comment_count'], inplace=True)

        self.__posts = posts

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
        return self.__posts

    def get_conteudo_original(self):
        return self.__published