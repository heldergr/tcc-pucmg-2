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