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

// Listar quantidade de categoria por pais
db.categories.aggregate(
    [     
        {         
            '$group': { 
                _id: '$country',
                'count': { '$sum': 1 }
            }     
        } 
    ]
)


// Results
{ "_id" : "Categoria:Parques nacionais da Argentina", "count" : 31 }
{ "_id" : "Categoria:Geografia da Argentina", "count" : 16 }
{ "_id" : "Categoria:Parques da Argentina", "count" : 4 }

// Set country for all (no criteria) the pages and categories
db.categories.updateMany(
    {},
    { "$set": { "country": "Argentina" }}
)
db.categories.updateMany(
    {},
    { $set, { country: "Argentina" }}
)

// Corrigir pages sem country
db.pages.updateMany( 
    { 
        "country": { "$exists": false } 
    }, 
    { 
        "$set": { "country": "Chile" } 
    } 
);

// Corrigir pages sem country
db.categories.updateMany( 
    { 
        "country": { "$exists": false } 
    }, 
    { 
        "$set": { "country": "Chile" } 
    } 
);

// Fix wrong country  in categories
ids_fix = [994848, 134030, 924189, 3177252, 4131772, 3455506, 3206668]
for id_fix in ids_fix:
    mongo_categories.update_many({"parent": id_fix}, {"$set": { "country": "Nova Zelandia"}})
    mongo_pages.update_many({"category_id": id_fix}, {"$set": { "country": "Nova Zelandia"}})
```