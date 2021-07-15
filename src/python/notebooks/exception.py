class FonteDeDadosNotFoundError(Exception):

    def __init__(self, fonte_de_dados):
        self.fonte_de_dados  = fonte_de_dados
        self.mensagem = f'A fonte de dados {fonte_de_dados} nao foi encontrada!'