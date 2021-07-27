# Modelo de dados da Wikipedia

## Estrutura de documentos

- **_id**: Id do documento no MongoDB
- **pageid**: Id da página na wikipedia
- **title**: Título da página na wikipedia
- **type**: Tipo do conteúdo. Originalmente quando veio da Wikipedia poderia ser *page* ou *categoria* mas nesta collection foram gravados apenas os que são páginas
- **download**: Status de download do conteúdo. 
- **country**: País ao qual se refere o conteúdo
- **categories**: Categorias nas quais uma página foi referenciada
- **wikitext**: Conteúdo original da página no formato wiki
- **text**: Conteúdo original da página no formato html. Inclui diversos marcadores, inclusive estilo. Conteúdo exato que veio da extração da API da wikipedia
- **text_clean**: Conteúdo original da página sem marcadores html. Obtido da extração do texto puro que estava originalmente no campo *text*.
- **text_processed**: Conteúdo sem palavras desnecessárias (por diversos motivos) pronto para ser trabalhado