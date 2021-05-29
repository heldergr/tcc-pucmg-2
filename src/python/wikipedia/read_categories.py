import requests

def download_membros_categorias(categorias):
    for categoria in categorias:
        print(f'Download de categoria {categoria["title"]}')

url = 'http://localhost:3000/categories?cmtitle=Category:Physics'

response = requests.get(url)

if (response.status_code == 200):
    jason = response.json()
    category_members = jason[0]['query']['categorymembers']
    download_membros_categorias(category_members)
else:
    print(f'Erro {response.status_code} ao executar requisicao')
