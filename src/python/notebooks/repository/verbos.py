from repository.mongo_utils import get_verbos_collection

class VerbosRepo:

    def __init__(self) -> None:
        self.__verbos_collection = get_verbos_collection()

    def find_all(self):
        return list(self.__verbos_collection.find({}))

    def find_all_stemmed(self):
        return self.__verbos_collection.distinct('verbo_stemmed')