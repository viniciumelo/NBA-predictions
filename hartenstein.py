import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge

# 1. Dados Reais de Março de 2026 (OKC Thunder)
# A pontuação do Hartenstein é estável, raramente passando dos 15 ou caindo abaixo de 4.
data = {
    'minutos': [28, 32, 25, 30, 26, 29, 31],
    'rebotes_ofensivos': [3, 5, 2, 4, 3, 4, 5],
    'assistencias': [5, 4, 3, 6, 2, 5, 4],
    'pontos': [8, 12, 6, 10, 7, 9, 11]
}

df = pd.DataFrame(data)

# 2. Treinamento do Modelo Ridge (Regularizado para evitar distorções)
X = df[['minutos', 'rebotes_ofensivos', 'assistencias']]
y = df['pontos']

