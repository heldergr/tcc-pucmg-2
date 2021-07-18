from repository.resultado import ResultadoRepo

import pandas as pd

resultado_repo = ResultadoRepo()

class ResultadoExplorer:

    def find_all(self):
        todos_resultados = resultado_repo.find_all()
        df = pd.DataFrame(todos_resultados)
        return df.drop(columns=['_id'])