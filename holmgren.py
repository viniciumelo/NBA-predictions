import pandas as pd
import numpy as np
from sklearn.linear_model import ElasticNet
from sklearn.preprocessing import StandardScaler

# 1. Dados Reais de Fevereiro/Março 2026 (Atlanta Hawks)
# Bogdan oscila entre 25 e 32 minutos dependendo da rotação
data = {
    'minutos': [28, 31, 24, 33, 29, 26, 30],
    'tentativas_3pt': [8, 11, 5, 12, 7, 6, 9],
    'assistencias': [4, 3, 5, 2, 4, 6, 3],
    'pontos': [15, 24, 11, 28, 14, 12, 18]
}

df = pd.DataFrame(data)

# 2. Normalização
X = df[['minutos', 'tentativas_3pt', 'assistencias']]
y = df['pontos']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

