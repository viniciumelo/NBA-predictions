import pandas as pd
import numpy as np
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler

# 1. Dados Reais de Fevereiro de 2026 (Charlotte Hornets)
# Inclui o jogo histórico de 10 bolas de 3pts contra Washington
data = {
    'minutos': [23, 27, 27, 31, 32, 28, 30],
    '3pt_feitos': [4, 10, 2, 1, 7, 3, 4],
    'pontos': [16, 37, 18, 11, 24, 15, 19]
}

df = pd.DataFrame(data)

# 2. Normalização e Treinamento
X = df[['minutos', '3pt_feitos']]
y = df['pontos']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

