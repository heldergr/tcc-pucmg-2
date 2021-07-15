from fonte_dados.nerds_viajantes import NerdsViajantes
from fonte_dados.wikipedia import Wikipedia
from util import constants

class FabricaFonteDados:

    def __init__(self):
        self.__fontes = {
            constants.NERDS_VIAJANTES: NerdsViajantes(carregar_previamente=False),
            constants.WIKIPEDIA: Wikipedia(carregar_previamente=False)
        }

    def get_fonte_dados(self, descricao):
        return self.__fontes.get(descricao, None)