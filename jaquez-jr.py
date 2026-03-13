import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# 1. Dados Reais de Março de 2026 (Miami Heat)
# Jaime tem uma minutagem bem estável entre 28 e 34 minutos
data = {
    'minutos': [28, 32, 35, 29, 31, 33, 30],
    'tentativas_fg': [9, 12, 14, 10, 11, 13, 11],
    'rebotes_ofensivos': [1, 3, 2, 1, 4, 2, 3],
    'pontos': [11, 16, 21, 13, 15, 18, 14]
}

df = pd.DataFrame(data)

# 2. Treinamento do Modelo
X = df[['minutos', 'tentativas_fg', 'rebotes_ofensivos']]
y = df['pontos']

# Random Forest captura bem as nuances de jogadores multifuncionais
modelo_jaime = RandomForestRegressor(n_estimators=100, random_state=42)
modelo_jaime.fit(X, y)
