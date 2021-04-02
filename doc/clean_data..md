# Limpeza de dados

## Normalização

* converter para lowercase
* remover pontuações, números e outros caracteres desnecessários (tipo hashtags)

## Stopwords

* remover palavras que aparecem com frequência e que atrapalham a interpretação dos tópicos do texto (e ainda têm custo computacional quando mantidas no dataset)
  * deve ter muito cuidado quando envolve análise de sentimento
* lista de stopwords pode ser incrementada dependendo do contexto da análise

## Stemming

* Processo de reduzir as palavras à forma raiz das mesmas
  * Exemplo: rains, raining, etc, converte para rain
* Também tem objetivo de reduzir ruído e dimensionalidade dos dados
* antes de fazer stemming deve-se tokenizar o texto
  * usando ferramenta apropriada, que é mais recomendado que simplesmente fazer split

## Lemmatization

* objetivo inicial é o mesmo de stemming, reduzir as palavras a sua forma raiz
* Stemming é uma forma mais crua de fazer o processo, enquanto a lematização faz uma análise morfológica mais profunda para definir a raiz de uma palavra (ou *lemma*)

## Part of speech (POS) tagging and chunking

* categoriza as palavras de acordo com a forma como a palavra atual no contexto
  * pode ser noun, verb, etc

## Referências

* [Text cleaning methods for natural language processing](https://towardsdatascience.com/text-cleaning-methods-for-natural-language-processing-f2fc1796e8c7)
