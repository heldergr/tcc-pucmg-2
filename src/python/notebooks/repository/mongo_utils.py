from pymongo import MongoClient

client = MongoClient()
wikipedia_db = client.wikipedia

def get_pages_content_collection():
    return wikipedia_db.pages_content

if __name__ == '__main__':
    pc = get_pages_content_collection()
    print(pc.count_documents({}))