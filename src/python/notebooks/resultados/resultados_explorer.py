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