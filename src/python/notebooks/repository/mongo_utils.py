from pymongo import MongoClient

client = MongoClient()

wikipedia_db = client.wikipedia
pucmg_db = client['tcc-pucmg']

def get_pages_content_collection():
    return wikipedia_db.pages_content

def get_verbos_collection():
    return pucmg_db.verbos

if __name__ == '__main__':
    pc = get_pages_content_collection()
    print(pc.count_documents({}))