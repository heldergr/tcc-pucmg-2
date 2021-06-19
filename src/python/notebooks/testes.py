from explore.wikipedia import WikipediaExplorer
from repository.wikipedia import WikipediaRepo
from repository.mongo_utils import get_pages_content_collection

if __name__ == '__main__':
    wikipedia_repo = WikipediaRepo(collection=get_pages_content_collection())
    wikipedia_explorer = WikipediaExplorer(wikipedia_repo)
    wikipedia_explorer.explore()
