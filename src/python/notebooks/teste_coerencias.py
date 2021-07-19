from fonte_dados.fabrica import FabricaFonteDados
from treinamento.coerencia import CalculadorCoerencia
from util import constants

import time

fabrica = FabricaFonteDados()

topicos_from = 5
topicos_to = 6

inicio = time.time()
fonte_dados_origem = fabrica.get_fonte_dados(constants.NERDS_VIAJANTES)
fonte_dados_origem.carregar_dados()

print(f'Calculando coerencia para o intervalo de topicos de {topicos_from} a {topicos_to}')

calculador_coerencia = CalculadorCoerencia(fonte_dados_origem)
coerencias = calculador_coerencia.calcular_coerencias(topicos_from, topicos_to, debug=True)
coerencias.to_csv(f'/home/helder/estudos/tcc-pucmg-2/src/python/notebooks/treinamento/coerencias_{topicos_from}-to-{topicos_to}.csv')

tempo_gasto = time.time() - inicio
print(f'O tempo gasto no calculo de coerencias foi {tempo_gasto:.2f} segundos.')