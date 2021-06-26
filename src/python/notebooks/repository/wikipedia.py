from pymongo import MongoClient

client = MongoClient()
wikipedia_db = client.wikipedia
pages_content = wikipedia_db.pages_content

class WikipediaRepo:

    def __init__(self, collection):
        self.collection = collection

    def find_all(self):
        return list(self.collection.find({}))

    def set_text_clean(self, id, text_clean):
        self.collection.update_one(
            { '_id': id },
            { '$set': { 'text_clean': text_clean } }
        )

if __name__ == '__main__':
    wikipedia_repo = WikipediaRepo(collection=pages_content)
    all_posts_content = wikipedia_repo.find_all()
    print(f'Foram retornados {len(all_posts_content)} posts com conteudo')
    print('Amostra de 5 posts:')

    import pprint

    pprint.pprint(all_posts_content[:5])