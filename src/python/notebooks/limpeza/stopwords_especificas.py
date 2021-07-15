from util import constants
from exception import FonteDeDadosNotFoundError

caminho_base_pasta_limpeza = '/home/helder/estudos/tcc-pucmg-2/src/python/notebooks/limpeza'
arquivos_limpeza_especificos = {
    constants.NERDS_VIAJANTES: f'{caminho_base_pasta_limpeza}/remocao_nerds_viajantes.txt'
}

class StopwordsSpecificas:

    def __init__(self) -> None:
        pass

    def carregar_palavras_especificas(self, fonte_de_dados):
        arquivo_limpeza_especificos = arquivos_limpeza_especificos.get(fonte_de_dados, None)
        if arquivos_limpeza_especificos:
            palavras = []
            with open(arquivo_limpeza_especificos) as f:
                palavras = f.readlines()

            palavras_formatadas = [p.split(' ')[0] for p in palavras]    
            return palavras_formatadas

        else:
            raise FonteDeDadosNotFoundError(fonte_de_dados)
