# Modelo de dados de post da wikipedia no MongoDB

## Métodos úteis para teste

- *db.collection.count()*
- *db.collection.find().pretty()*

## Collections

- categories
    * id
    * title
- pages
    * id
    * title
    * category_id
    * category_title
    * content
    * downloaded

## Useful commands

```javascript
db.categories.find()

db.categories.count()

db.categories.deleteMany({})

db.categories.updateMany(
    {},
    { "$set", {} }
)

// Contar categorias para avaliar download
db.categories.count({"download": 'Check'})

// Contar categorias que foram feitos download
db.categories.count({"download": 'Done'})

// Contar categorias aguardando download
db.categories.count({"download": 'Waiting'})

// Listar quantidade de páginas por categoria
db.pages.aggregate(
    [     
        {         
            '$group': { 
                _id: '$category_title',
                'count': { '$sum': 1 }
            }     
        } 
    ]
)

// Results
{ "_id" : "Categoria:Parques nacionais da Argentina", "count" : 31 }
{ "_id" : "Categoria:Geografia da Argentina", "count" : 16 }
{ "_id" : "Categoria:Parques da Argentina", "count" : 4 }
```