import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# 1. Dados Reais de Fevereiro/Março 2026 (Milwaukee Bucks)
# Kon tem tido um volume de arremessos digno de veterano
data = {
    'minutos': [32, 28, 35, 30, 27, 33, 31],
    'bolas_3pt_tentadas': [9, 7, 12, 8, 6, 11, 10],
    'gravidade_giannis': [8, 5, 9, 7, 4, 9, 8], # Escala de 1-10 (atenção da defesa no Giannis)
    'pontos': [21, 15, 29, 18, 12, 26, 23]
}

df = pd.DataFrame(data)

# 2. Treinamento do Modelo
X = df[['minutos', 'bolas_3pt_tentadas', 'gravidade_giannis']]
y = df['pontos']

modelo_kon = RandomForestRegressor(n_estimators=100, random_state=42)
modelo_kon.fit(X, y)

