# Tarefas

## Coleta e limpeza de dados

* O cálculo de coerência foi feito com os valores default de alpha e eta, que são 1/número de tópicos.
  * Após selecionar os 7 números de tópicos mais relevantes, calcular a coerência com o intervalo de eta e alpha escolhidos para os testes
  * Dar ênfase especial a tupla (num_topics, alpha, etc), que contribuem com a maior coerencia
* Executar baterias de testes
    * Fonte: sempre nerds viajantes
    * Destino: fazer para nerds viajantes e wikipedia
    * Parâmetros a variar
        * num_topics, eta, alpha
    * Usando nerds
* Baixar páginas da wikipedia
    * Parques nacionais do Brasil
    * Reservas do Brasil
    * Parques estaduais do Brasil
* :heavy_check_mark: Refatoração de código - mover código de notebooks para módulos
    * analise-palavras-fontes-dados.ipynb
* :heavy_check_mark: Remover tags html do texto
* :heavy_check_mark: Remover stopwords em português
* :heavy_check_mark: Fazer stemming em português
* :heavy_check_mark: Remover posts dos papéis de parede e outros desnecessários
* :heavy_check_mark:Elaborar lista com stopwords customizáveis, palavras que aparecem muito nos textos mas que não são interessantes do ponto de vista da classificação
  * Sugestões: download, &nbsp (avaliar em posts de verdade), blog
* :heavy_check_mark: Remover textos entre colchetes (Exemplo: [caption ... ])
* :heavy_check_mark: Remover propaganda do booking no final do texto 

### Wikipedia
- Categorias Parques Nacionais
    * [Categoria: Parques Nacionais do Chile](https://pt.wikipedia.org/w/api.php?action=query&list=categorymembers&cmtitle=Category:Parques_nacionais_do_Chile&cmlimit=500)
    * [Categoria: Parques Nacionais da Argentina](https://pt.wikipedia.org/wiki/Categoria:Parques_nacionais_da_Argentina)
    * [Categoria: Parques Nacionais de Bolivia](https://pt.wikipedia.org/wiki/Categoria:Parques_nacionais_da_Bol%C3%ADvia)
    * [Categoria: Parques Nacionais da Nova Zelândia](https://pt.wikipedia.org/wiki/Categoria:Parques_nacionais_da_Nova_Zel%C3%A2ndia)
- Páginas Parques Nacionais
    * [Página: Parque Nacional (Bom índice)](https://pt.wikipedia.org/wiki/Parque_nacional)
    * [Página: Lista de Parques Nacionais dos Estados Unidos](https://pt.wikipedia.org/wiki/Lista_de_parques_nacionais_dos_Estados_Unidos)
- Outros
    * [Pesquisa por página individual](https://pt.wikipedia.org/w/api.php?action=parse&pageid=2535813&prop=wikitext&formatversion=2)
    * Geolocation
        * [Posts próximos a El Chaltén](https://en.wikipedia.org/w/api.php?action=query&list=geosearch&gscoord=-49.32495125885588|-72.89174154002943&gsradius=10000&gslimit=100)
        * [Posts próximos a Bariloche](https://pt.wikipedia.org/w/api.php?action=query&list=geosearch&gscoord=-41.138115588301886|-71.30968382175735&gsradius=10000&gslimit=100)

## Treinamento

* Excelente post: [https://towardsdatascience.com/basic-nlp-on-the-texts-of-harry-potter-topic-modeling-with-latent-dirichlet-allocation-f3c00f77b0f5](https://towardsdatascience.com/basic-nlp-on-the-texts-of-harry-potter-topic-modeling-with-latent-dirichlet-allocation-f3c00f77b0f5)
  * Checar [código fonte](https://github.com/raffg/harry_potter_nlp/blob/master/LDA.ipynb)

## Similaridade entre textos

* Usando LDA
  * [https://www.kaggle.com/ktattan/lda-and-document-similarity](https://www.kaggle.com/ktattan/lda-and-document-similarity)

## Comparações

- Interna
    * Entre os próprios posts do blog
- Externa
    * Wikipedia: Argentina? Parques Nacionais?
    * Melhores Destinos
    * Twitter

## Trabalho futuro

* Melhores Destinos
  * Ideia: pegar um intervalo de paginas de indices de promocoes, baixar as promocoes do intervalo e treinar com elas
  * https://www.melhoresdestinos.com.br/promocao/page/300
* Avaliar uso de collocations
* Análise de distribuição de tokens por documento após fazer limpezas
  * Mostrar histograma com tamanho (len(tokenized)) dos documentos
* Avaliar eliminação de palavras por frequência
  * Para o LDA é muito importante eliminar stopwords e palavras raras para evitar de o modelo fazer sobrecompensação
* Avaliar variações dos parâmetros alpha (tópicos em documentos) e eta (palavras em tópicos)
* Testar diferentes tipos de stemmer
* Avaliar uso de biterm model para documentos pequenos
  * [Referência](https://pdfs.semanticscholar.org/f499/5dc2a4eb901594578e3780a6f33dee02dad1.pdf)
* [Testar com algoritmo PLSA](https://towardsdatascience.com/topic-modelling-with-plsa-728b92043f41)
* Testes sem remoção de stopwords
* Explicar porque não foi feito lematização e part of speech em português


### Documentação

- Partes
    * Motivação
    * Limpeza de dados
    * Coleta de dados
    * Algoritmos e estruturas de dados
    * Exploração de dados
    * Semelhança entre documentos
    * :heavy_check_mark: Coerência
    * Trabalho futuro
    * Tecnologias
    * Link
    * Referência
    * Código fonte
    * Treinamento
    * Resultados

- Após o treinamento, pegar um texto e mostrar graficamente a distribuição de tópicos para aquela documento, conforme exemplo no post [https://www.kaggle.com/ktattan/lda-and-document-similarity](https://www.kaggle.com/ktattan/lda-and-document-similarity)