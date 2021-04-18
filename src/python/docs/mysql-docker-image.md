# Como usar a imagem do Mysql

MySql local


* Executando o MySql localmente
* Eu usei a tag latest para ter a versão mais recente da imagem
* *my-secret-pw* é o valor atribuído à variável de ambiente *MYSQL_ROOT_PASSWORD*, que é a senha do usuário root

```terminal
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:tag
```

## Imagem com sql dump carregado

### Dockerfile

COLAR AQUI CONTEUDO DO DOCKERFILE

### Criar imagem

Ir para diretório onde está o arquivo Dockerfile ($PROJECT/docker).

```terminal
docker build -t heldergr/tcc-mysql:1.0.0 .
```

## Volume de dados

```terminal
docker volume create tcc-mysql-vol
```

Executando o container com o volume

```terminal
docker run -d --name tcc-mysql -v tcc-mysql-vol/var/lib/mysql -p 3306:3306 heldergr/tcc-mysql:1.0.1
```

## Interagindo com o container

Executando comandos no container

```terminal
docker exec -it tcc-mysql bash -l

# Inside the container
mysql -uroot -proot

# List databases
Select database();

Use tcc;

Show tables;

— 10054
select count(*) from wp_eeurng_posts;

— return 311 (se parece mais com a lista de posts do blog)
select count(*) from wp_us3xyq_posts; 
```

## Explorando os dados

Usando os comandos da seção anterior foi possível explorar os dados dos posts do blog. Há dois padrões de nomes de tabelas e ao que parece eles se referem aos posts do blog da época que era nerdsviajantes.wordpress.com (us3xyq) e www.nerdsviajantes.com (eeurng). 

A tabela onde são gravados os posts parece ser a wp-*-posts (verificar colunas post_date e post_content).
	
### Tabela de posts

```terminal
mysql> DESCRIBE wp_us3xyq_posts;
+-----------------------+-----------------+------+-----+---------------------+----------------+
| Field                 | Type            | Null | Key | Default             | Extra          |
+-----------------------+-----------------+------+-----+---------------------+----------------+
| ID                    | bigint unsigned | NO   | PRI | NULL                | auto_increment |
| post_author           | bigint unsigned | NO   | MUL | 0                   |                |
| post_date             | datetime        | NO   |     | 0000-00-00 00:00:00 |                |
| post_date_gmt         | datetime        | NO   |     | 0000-00-00 00:00:00 |                |
| post_content          | longtext        | NO   |     | NULL                |                |
| post_title            | text            | NO   |     | NULL                |                |
| post_excerpt          | text            | NO   |     | NULL                |                |
| post_status           | varchar(20)     | NO   |     | publish             |                |
| comment_status        | varchar(20)     | NO   |     | open                |                |
| ping_status           | varchar(20)     | NO   |     | open                |                |
| post_password         | varchar(20)     | NO   |     |                     |                |
| post_name             | varchar(200)    | NO   | MUL |                     |                |
| to_ping               | text            | NO   |     | NULL                |                |
| pinged                | text            | NO   |     | NULL                |                |
| post_modified         | datetime        | NO   |     | 0000-00-00 00:00:00 |                |
| post_modified_gmt     | datetime        | NO   |     | 0000-00-00 00:00:00 |                |
| post_content_filtered | longtext        | NO   |     | NULL                |                |
| post_parent           | bigint unsigned | NO   | MUL | 0                   |                |
| guid                  | varchar(255)    | NO   |     |                     |                |
| menu_order            | int             | NO   |     | 0                   |                |
| post_type             | varchar(20)     | NO   | MUL | post                |                |
| post_mime_type        | varchar(100)    | NO   |     |                     |                |
| comment_count         | bigint          | NO   |     | 0                   |                |
+-----------------------+-----------------+------+-----+---------------------+----------------+
```

## Referências

* [Imagem Docker MySql](https://hub.docker.com/_/mysql)
