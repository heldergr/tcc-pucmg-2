import yaml
import itertools

class EspecificacaoTestes:

    def __init__(self, filaname):
        self.__filename = filaname

    def get_testes(self):
        with open(self.__filename, 'r') as spec:
            try:
                return yaml.safe_load(spec)
            except yaml.YAMLError as exc:
                print(exc)

if __name__ == '__main__':
    filename = '/home/helder/estudos/tcc-pucmg-2/src/python/notebooks/main/especificacao_2.yml'
    especificacao_testes = EspecificacaoTestes(filename)
    cenarios = especificacao_testes.get_testes()
    print(cenarios)
    for cenario in cenarios:
        topics = cenario['topics']
        etas = cenario['eta']
        alphas = cenario['alpha']
        passes = cenario['passes']
        print(topics)
        print(etas)
        print(alphas)
        print(passes)
        ps = itertools.product(topics, etas, alphas, passes)
        for p in ps:
            num_topics, eta, alpha, passes = p
            print(f'num_topics={num_topics}, eta={eta}, alpha={alpha}, passes={passes}')
