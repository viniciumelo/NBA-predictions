import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# 1. Dados Reais de Fevereiro de 2026 (Logs de Jogos)
# Wemby oscila minutos devido a placares elásticos (blowouts)
data = {
    'minutos': [33, 26, 27, 34, 28, 27, 30, 28],
    'tentativas_3pts': [9, 6, 6, 9, 2, 4, 3, 3],
    'pontos': [26, 40, 16, 29, 22, 25, 16, 28]
}

df = pd.DataFrame(data)

# 2. Treinamento do Modelo
X = df[['minutos', 'tentativas_3pts']]
y = df['pontos']

modelo = RandomForestRegressor(n_estimators=100, random_state=42)
modelo.fit(X, y)

# 3. Predição para o próximo jogo contra o Phoenix Suns (19/02/2026)
# Projeção: Jogo equilibrado (32 min) e ele deve chutar umas 7 bolas de fora
proximo_jogo = np.array([[32, 7]])
predicao = modelo.predict(proximo_jogo)

