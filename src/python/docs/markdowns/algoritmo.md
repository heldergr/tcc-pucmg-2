# Algoritmo

## Definições

- **Conteúdo de treinamento**: Conteúdo que será usado como base para a definição dos tópicos. Com base neste conteúdo será gerado o dicionário de palavras a ser usado em todo o trabalho
- **Conteúdo de comparação**: Conteúdo que será usado para obter seus tópicos e posterior comparação com conteúdo de treinamento. A ideia do trabalho é encontrar no conteúdo de comparação documentos similares aos do conteúdo de treinamento

## Algoritmo

1. Trabalhar conteúdo de treinamento (Posts do blog Nerds Viajantes)
    * Ler posts do repositório
    * Remover posts desnecessários
    * Limpar textos
    * Gerar dicionário de palavras (Mapeamento de palavra para id)
        * Gravar em repositório local para uso no treinamento das bases de comparação
    * Criar corpus com conteúdo de treinamento
    * Fazer treinamento utilizando LDA
    * Definir tópicos para cada post
        * Gravar em repositorio local para posterior comparação
2. Trabalhar conteúdo 
