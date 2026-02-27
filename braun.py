import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor

# 1. Dados Reais de Fevereiro de 2026 (Denver Nuggets)
# Reflete o aumento de volume com a ausência de titulares
data = {
    'minutos': [24, 32, 35, 28, 31, 38, 30],
    'tentativas_fg': [6, 11, 14, 9, 10, 15, 12],
    'pontos_transicao': [4, 6, 8, 2, 4, 10, 6],
    'pontos': [8, 14, 19, 11, 12, 22, 15]
}

df = pd.DataFrame(data)

# 2. Treinamento do Modelo
X = df[['minutos', 'tentativas_fg', 'pontos_transicao']]
y = df['pontos']

# Árvore de decisão para capturar o "teto" de esforço do Braun
modelo_braun = DecisionTreeRegressor(max_depth=3, random_state=42)
modelo_braun.fit(X, y)

# 3. Predição para o jogo de hoje contra OKC (27/02/2026)
# Projeção: Sem Aaron Gordon, Braun deve jogar muito (34 min) e correr a quadra
proximo_jogo = np.array([[34, 12, 6]]) 
predicao = modelo_braun.predict(proximo_jogo)

