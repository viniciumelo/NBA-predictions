import pandas as pd
import numpy as np
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler

# 1. Dados Reais de Fevereiro de 2026 (Detroit Pistons)
# Cade tem tido jogos de alto volume de arremessos (20+)
data = {
    'minutos': [34, 38, 32, 36, 35, 37, 30],
    'usage_rate': [28.5, 33.1, 26.0, 31.4, 30.2, 34.0, 25.5],
    'pontos': [22, 31, 19, 26, 25, 34, 18]
}

df = pd.DataFrame(data)

# 2. Normalização e Treinamento
X = df[['minutos', 'usage_rate']]
y = df['pontos']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# SVR para lidar com a variação de volume do Cade
modelo_cade = SVR(kernel='rbf', C=100, gamma=0.1)
modelo_cade.fit(X_scaled, y)

