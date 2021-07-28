from pymongo import MongoClient

client = MongoClient()

wikipedia_db = client.wikipedia
pucmg_db = client['tcc-pucmg']

def get_wikipedia_collection(collection_name):
    return wikipedia_db[collection_name]

def get_pages_content_collection():
    return wikipedia_db.pages_content

def get_verbos_collection():
    return pucmg_db.verbos

def get_resultados_collection(collection_name=None):
    if collection_name is not None:
        return pucmg_db[collection_name]
    else:
        return pucmg_db.resultados

if __name__ == '__main__':
    pc = get_pages_content_collection()
    print(pc.count_documents({}))