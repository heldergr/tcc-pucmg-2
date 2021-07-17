from fonte_dados.fabrica import FabricaFonteDados
from limpeza.stopwords_especificas import StopwordsSpecificas
from repository.verbos import VerbosRepo
from limpeza.stopwords_especificas import StopwordsSpecificas

import numpy as np
import pandas as pd

fabrica = FabricaFonteDados()

verbo_repo = VerbosRepo()
verbos_stemmed = verbo_repo.find_all_stemmed()

stopwords_especificas = StopwordsSpecificas()

def obter_tokens_nao_verbo(documento):
    return [token for token in documento if token not in verbos_stemmed]

def obter_documentos_sem_verbo(documentos):
    return [obter_tokens_nao_verbo(documento) for documento in documentos]

def obter_tokens_nao_stopwords(documento, stopwords):
    return [token for token in documento if token not in stopwords]

def obter_documentos_sem_stopwords(documentos, stopwords):
    return [obter_tokens_nao_stopwords(documento, stopwords) for documento in documentos]

def obter_tamanhos_documentos(documentos):
    return [len(doc) for doc in documentos]

def obter_informacoes_palavras(descricao_fonte_de_dados, limpar_stopwords_especificas=False, limpar_verbos=False):
    fonte_dados_origem = fabrica.get_fonte_dados(descricao_fonte_de_dados)
    fonte_dados_origem.carregar_dados(limpar_stopwords_especificas=limpar_stopwords_especificas, limpar_verbos=limpar_verbos)
    
    documentos_origem = fonte_dados_origem.get_tokens()
    tamanhos_documentos = obter_tamanhos_documentos(documentos_origem)
    
    documentos_sem_verbo = obter_documentos_sem_verbo(documentos_origem)
    tamanhos_sem_verbo = obter_tamanhos_documentos(documentos_sem_verbo)
    percentual_nao_verbo = 100 * (np.array(tamanhos_sem_verbo) / np.array(tamanhos_documentos))

    stopwords = stopwords_especificas.carregar_palavras_especificas(descricao_fonte_de_dados)
    documentos_sem_verbo_sw = obter_documentos_sem_stopwords(documentos_sem_verbo, stopwords)
    tamanhos_sem_verbo_sw = obter_tamanhos_documentos(documentos_sem_verbo_sw)
    percentual_nao_verbo_sw = 100 * (np.array(tamanhos_sem_verbo_sw) / np.array(tamanhos_documentos))

    return pd.DataFrame(
        data = { 
            'documento': documentos_origem, 
            'tamanho': tamanhos_documentos, 
            'documento_nao_verbo': documentos_sem_verbo, 
            'tamanho_sem_verbo': tamanhos_sem_verbo,
            'percentual_nao_verbo': percentual_nao_verbo,
            'documento_nao_verbo_sw': documentos_sem_verbo_sw, 
            'tamanho_sem_verbo_sw': tamanhos_sem_verbo_sw,
            'percentual_nao_verbo_sw': percentual_nao_verbo_sw
        })