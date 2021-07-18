from repository.mongo_utils import get_resultados_collection

"""
Repositorio para resultado de analise de semelhanca entre documentos. 

Cada documento aqui gravado deve conter os seguintes campos:
- id_cenario: identificador do cenário de treinamento
- fonte_origem: fonte de dados de origem
- id_documento_origem: identificador do documento de origem
- titulo_documento_origem: título do documento de origem
- fonte_destino: fonte de dados de destino
- id_documento_destino: identificador do documento de destino
- titulo_documento_destino: título do documento de destino
- distancia_destino: Distancia entre documento de origem e destino
"""
class ResultadoRepo:

    def __init__(self) -> None:
        self.__resultados_collection = get_resultados_collection()

    def insert_many(self, resultados):
        self.__resultados_collection.insert_many(resultados)

    def __find(self, criteria):
        return list(self.__resultados_collection.find(criteria))

    def find_all(self):
        return self.__find({})