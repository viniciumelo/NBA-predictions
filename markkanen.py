import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler

# 1. Dados Reais de Março de 2026 (Utah Jazz)
# Markkanen é a primeira opção ofensiva clara do Jazz
data = {
    'minutos': [32, 35, 30, 36, 34, 38, 33],
    'tentativas_3pt': [8, 11, 6, 9, 7, 12, 10],
    'lances_livres_tentados': [5, 8, 4, 7, 6, 9, 6],
    'pontos': [21, 29, 18, 26, 22, 34, 25]
}

df = pd.DataFrame(data)

# 2. Normalização e Treinamento
X = df[['minutos', 'tentativas_3pt', 'lances_livres_tentados']]
y = df['pontos']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Ridge ajuda a lidar com a variação do chute de 3pts
modelo_lauri = Ridge(alpha=1.0)
modelo_lauri.fit(X_scaled, y)
