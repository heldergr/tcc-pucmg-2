from fonte_dados.nerds_viajantes import NerdsViajantes
from fonte_dados.wikipedia import Wikipedia

NERDS_VIAJANTES = 'NERDS_VIAJANTES'
WIKIPEDIA = 'WIKIPEDIA'

class FabricaFonteDados:

    def __init__(self):
        self.__fontes = {
            NERDS_VIAJANTES: NerdsViajantes(carregar_previamente=False),
            WIKIPEDIA: Wikipedia(carregar_previamente=False)
        }

    def get_fonte_dados(self, descricao):
        return self.__fontes.get(descricao, None)