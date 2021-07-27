# Uso do MongoDB

- [Usando MongoDB com Docker](#usando_mmongodb_com_docker)
- [Uso básico do MongoDB](#uso_b_sico_do_mongodb)
- [Referências](#refer_ncias)

## Usando MongoDB com Docker

```bash
# Listar volumes existentes:
docker volume ls

# Criar volume para mongo
docker volume create mongo-vol

# Download da imagem
docker pull mongo

# Criar e executar container
# 27017 é a porta padrão do mongodb
# A configuração default do mongodb não tem username/password, que devem ser configurados a parte se for necessário
docker run --name tcc-mongo -v mongo-vol:/data/db -p 27017:27017 -d mongo

# Conectando ao shell do container
docker exec -it tcc-mongo bash
```

## Uso básico do MongoDB

```bash
# Checar banco em uso
db

# Mudar de banco
# Obs: Não precisa criar collection a priori. No primeiro uso ela é criada
use tcc-pucmg

# Exemplos de uso
> db.textos.find().pretty()
> db.textos.insertOne({ x:1 })
{
	"acknowledged" : true,
	"insertedId" : ObjectId("60ad0aad02f6dca32b307dfe")
}
> db.textos.find().pretty()
{ "_id" : ObjectId("60ad0aad02f6dca32b307dfe"), "x" : 1 }
```

## Referêncisa

- [MongoDB Guides](https://docs.mongodb.com/guides)