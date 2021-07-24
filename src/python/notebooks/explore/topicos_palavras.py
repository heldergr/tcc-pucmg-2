from fonte_dados.fabrica import FabricaFonteDados
from treinamento.treinamento_lda import TreinamentoLda

from collections import Counter
import re

def treinar_modelo(fonte_origem, num_topics, limpar_stopwords_especificas=False, limpar_verbos=False):
    fabrica = FabricaFonteDados()

    # Carregar fonte de dados de origem
    fonte_dados_origem = fabrica.get_fonte_dados(fonte_origem)
    fonte_dados_origem.carregar_dados(limpar_stopwords_especificas=limpar_stopwords_especificas, limpar_verbos=limpar_verbos)
    documentos_origem = fonte_dados_origem.get_tokens()

    # Ajuste de modelo
    treinamento_lda = TreinamentoLda(num_topics=num_topics, passes=2)
    resultado_lda = treinamento_lda.ajustar_modelo(documentos_origem)
    lda = resultado_lda.modelo_lda
    return lda

def extrair_palavras(descricao_palavra):
    return re.findall('\".+?\"', descricao_palavra)

"""
Faz analise das top n palavras que mais contribuem para as definicoes dos topics. Se o parametros topn nao eh informado apenas a palavras que mais contribue sera 
considerada. Se for informado 3, por exemplo, as 3 palavras que mais contribuem para um topico serao consideradas.

Retorno: tupla de 2 elementos onde o primeiro eh a lista de topicos com as topn palavras que mais contribuem e o segundo elemento eh um objeto counter que 
mostra as palavras que mais contribuem entre as topn dos topicos.
"""
def analisar_top_n_palavras_em_topicos(lda, num_topics, topn=1):
    topicos = lda.show_topics(num_topics=num_topics, num_words=topn)
    palavras_topicos = [extrair_palavras(p[1]) for p in topicos]
    topn_palavras = [palavra for palavras_topico in palavras_topicos for palavra in palavras_topico]
    print(f'len of top n palavras = {len(topn_palavras)}')
    counter_topn_palavras = Counter(topn_palavras)
    return (topicos, counter_topn_palavras.most_common())

"""
Recebe uma analise das topn palavras que mais contribuem para os topicos e extrai apenas os nomes das palavras.
"""
def extrair_palavras_candidatas(analise_topn):
    palavras = [f'{p[0][1:-1]} - {p[1]}' for p in analise_topn[1]]
    return palavras

pasta_limpeza = '/home/helder/estudos/tcc-pucmg-2/src/python/notebooks/data'
arquivo_candidatas_remocao = f'{pasta_limpeza}/candidatas_remocao_nerds_viajantes.txt'

def registrar_palavras_candidatas(analise_topn):
    palavras_candidatas = extrair_palavras_candidatas(analise_topn)
    with open(arquivo_candidatas_remocao, 'w') as f:
        for palavra in palavras_candidatas:
            f.write(f'{palavra}\n')