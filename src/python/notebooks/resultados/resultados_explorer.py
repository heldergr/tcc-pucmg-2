from repository.resultado import ResultadoRepo

import pandas as pd
import seaborn as sns

resultado_repo_wp_full = ResultadoRepo(collection_name='resultados-wp-full')
resultado_repo_wp_get42 = ResultadoRepo(collection_name='resultados')

def find_all_resultados():
    resultados_wp_full = resultado_repo_wp_full.find_all()
    resultados_wp_gte42 = resultado_repo_wp_get42.find_all()

    df_full = pd.DataFrame(resultados_wp_full)
    df_full['cenario_wp'] = 'full'
    df_gte42 = pd.DataFrame(resultados_wp_gte42)
    df_gte42['cenario_wp'] = 'gte42'

    return pd.concat([df_full, df_gte42])

def distribuicao_distancias(resultados, hue='cenario_wp'):
    ax = sns.displot(resultados, x='distancia_destino', kind='hist', aspect=1.2, hue=hue, kde=True)
    ax.set(xlabel='Distância entre documentos', ylabel='Frequência', title='Distribuição da distância entre documentos')

def distribuicao_distintos_destino_por_parametro(resultados, parametro):
    grouped_origem = resultados.groupby(['id_documento_origem', parametro])
    grouped_origem = grouped_origem.agg({'id_documento_destino': 'nunique'}).reset_index()
    ax = sns.displot(grouped_origem, x='id_documento_destino', kind='hist', aspect=1.2, kde=True, hue=parametro)
    ax.set(xlabel='Documentos distintos recomendados por origem', ylabel='Frequência', 
        title='Quantidade documentos distintos recomendados por origem')

def destinos_distintos_por_parametro(resultados, parametro, parametros_distintos=None):
    grouped_parametro = resultados.groupby(['id_documento_origem', parametro])
    grouped_parametro = grouped_parametro.agg({'id_documento_destino': 'nunique'}).reset_index().sort_values(by='id_documento_destino')
    if parametros_distintos is not None:
        grouped_parametro['possiveis'] = 336 / parametros_distintos
    return grouped_parametro

def adicionar_informacoes_posts(rs, posts, paginas):
    # Adiciona info posts
    mg = rs.merge(posts[['id_documento', 'nome']], left_on='id_documento_origem', right_on='id_documento')
    mg.drop(columns=['id_documento'], inplace=True)
    mg.rename(columns={'nome': 'nome_nv'}, inplace=True)

    # adiciona info paginsa
    mg = mg.merge(paginas[['id_documento', 'nome']], left_on='id_documento_destino', right_on='id_documento', how='left')
    mg.drop(columns=['id_documento'], inplace=True)
    mg.rename(columns={'nome': 'nome_wp'}, inplace=True)

    return mg

def obter_topn_recomendacoes_por_post(rs, id_post, n):
    rs_post = rs[rs['id_documento_origem'] == id_post]
    colunas_retorno = ['titulo_documento_origem', 'id_documento_destino', 'titulo_documento_destino']
    return rs_post.groupby(colunas_retorno).size().sort_values(ascending=False).iloc[:n,]

def obter_topn_posts_por_recomendado(rs, id_recomendado, n):
    resultados_rec = rs[rs['id_documento_destino'] == id_recomendado]
    print(resultados_rec.shape)
    return resultados_rec.groupby(['id_documento_origem', 'titulo_documento_origem']).size().sort_values(ascending=False)[:n,]