from pymongo import MongoClient

mongo_client = MongoClient()
db = mongo_client.wikipedia

"""
## Correção collection pages

- Problema: a mesma página tinha sido baixada mais de uma vez porque era referenciada por várias coleções
- Solução
    * Renomear collection pages para pages_incorreto (feito no mongo shell)
    * Recriar a collection pages com estrutura correta
        * A categoria agora será um objeto com id e título ao invés de estes valores estarem soltos na páginas. Assim ficará melhor estuturado
        * O objeto da página terá uma collection de categorias. Cada página lida da estrutura antiga terá na nova collection um array com as categorias que a referenciam
    * Renomear pages_content para pages_content incorreto
"""
class CorretorEstruturaCategorias:

    def __init__(self, collection_name_incorreto, collection_name_correto) -> None:
        self.__collection_incorreto = db[collection_name_incorreto]
        self.__collection_correto = db[collection_name_correto]

    def corrigir_categorias(self):
        todas_paginas_incorreto = list(self.__collection_incorreto.find({}))
        todas_paginas_incorreto = self.criar_objetos_categoria(todas_paginas_incorreto)
        agregado_paginas_incorreto = self.agregar_categorias_por_pagina(todas_paginas_incorreto)
        paginas_agregadas = list(agregado_paginas_incorreto.values())
        self.__collection_correto.insert_many(paginas_agregadas)

    def agregar_categorias_por_pagina(self, todas_paginas_incorreto):
        # Dictionario que mapeia uma pageid para documento da pagina
        agregado_paginas_incorreto = {}

        for pagina_incorreto in todas_paginas_incorreto:
            pageid_incorreto = pagina_incorreto['pageid']
            if pageid_incorreto in agregado_paginas_incorreto:
                existente = agregado_paginas_incorreto[pageid_incorreto]
                existente['categories'].append(pagina_incorreto['category'])
            else:
                pagina_incorreto['categories'] = [pagina_incorreto['category']]
                agregado_paginas_incorreto[pageid_incorreto] = pagina_incorreto
            del pagina_incorreto['category']
        
        return agregado_paginas_incorreto

    def criar_objetos_categoria(self, todas_paginas_incorreto):
        # Corrigir categoria das paginas incorretas. Cria objeto para categoria e coloca id e titulo
        for pagina_incorreto in todas_paginas_incorreto:
            category = {
                'category_id': pagina_incorreto['category_id'],
                'category_title': pagina_incorreto['category_title']
            }
            pagina_incorreto['category'] = category
            del pagina_incorreto['category_id']
            del pagina_incorreto['category_title']
        return todas_paginas_incorreto
