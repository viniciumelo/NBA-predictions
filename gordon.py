import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor

# 1. Dados Reais de Fevereiro/Março 2026 (Denver Nuggets)
# Focando no retorno dele após a lesão
data = {
    'minutos': [28, 32, 25, 30, 34, 22, 31],
    'assitencias_recebidas_jokic': [5, 8, 4, 7, 9, 3, 6],
    'aproveitamento_fg': [0.50, 0.55, 0.48, 0.60, 0.52, 0.45, 0.53],
    'pontos': [12, 18, 10, 15, 20, 8, 14]
}

df = pd.DataFrame(data)

# 2. Treinamento do Modelo KNN
# O modelo busca jogos onde a conexão com o Jokic foi similar
X = df[['minutos', 'assitencias_recebidas_jokic']]
y = df['pontos']

