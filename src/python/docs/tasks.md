# Tarefas

## Coleta e limpeza de dados

* Remover tags html do texto
* Remover stopwords em português
* Fazer stemming em português
* Remover posts dos papéis de parede e outros desnecessários
* Elaborar lista com stopwords customizáveis, palavras que aparecem muito nos textos mas que não são interessantes do ponto de vista da classificação
  * Sugestões: download, &nbsp (avaliar em posts de verdade), blog
* Remover textos entre colchetes (Exemplo: [caption ... ])

## Treinamento

* Excelente post: [https://towardsdatascience.com/basic-nlp-on-the-texts-of-harry-potter-topic-modeling-with-latent-dirichlet-allocation-f3c00f77b0f5](https://towardsdatascience.com/basic-nlp-on-the-texts-of-harry-potter-topic-modeling-with-latent-dirichlet-allocation-f3c00f77b0f5)
  * Checar [código fonte](https://github.com/raffg/harry_potter_nlp/blob/master/LDA.ipynb)

## Similaridade entre textos

* Usando LDA
  * [https://www.kaggle.com/ktattan/lda-and-document-similarity](https://www.kaggle.com/ktattan/lda-and-document-similarity)

## Trabalho futuro

* Avaliar uso de collocations
* Avaliar eliminação de palavras por frequência
  * Para o LDA é muito importante eliminar stopwords e palavras raras para evitar de o modelo fazer sobrecompensação
* Avaliar variações dos parâmetros alpha (tópicos em documentos) e eta (palavras em tópicos)
* Testar diferentes tipos de stemmer
* Avaliar uso de biterm model para documentos pequenos
  * [Referência](https://pdfs.semanticscholar.org/f499/5dc2a4eb901594578e3780a6f33dee02dad1.pdf)

### Documentação

* Após o treinamento, pegar um texto e mostrar graficamente a distribuição de tópicos para aquela documento, conforme exemplo no post [https://www.kaggle.com/ktattan/lda-and-document-similarity](https://www.kaggle.com/ktattan/lda-and-document-similarity)
