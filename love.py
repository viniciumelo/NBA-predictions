import pandas as pd
import numpy as np
from sklearn.linear_model import Lasso

# 1. Dados Reais de Fevereiro de 2026 (Utah Jazz)
# Love oscila dependendo do matchup (se o adversário tem pivôs lentos)
data = {
    'minutos': [16, 12, 15, 24, 13, 21, 18],
    'tentativas_3pt': [5, 3, 3, 4, 1, 3, 5],
    'rebotes_totais': [9, 6, 5, 11, 4, 11, 3],
    'pontos': [5, 13, 4, 3, 5, 6, 11]
}

df = pd.DataFrame(data)

# 2. Modelo Lasso (Focado em variáveis de impacto real)
X = df[['minutos', 'tentativas_3pt', 'rebotes_totais']]
y = df['pontos']

# Alpha baixo para manter a sensibilidade ao volume de 3pts
modelo_love = Lasso(alpha=0.1)
modelo_love.fit(X, y)

# 3. Predição para o jogo contra o New Orleans Pelicans (26/02/2026)
# Projeção: Jogo físico, ele deve jogar uns 14 min, tentar 3 bolas de fora e pegar 5 rebotes
proximo_jogo = np.array([[14, 3, 5]])
predicao = modelo_love.predict(proximo_jogo)

print(f"--- Projeção Kevin Love (UTA) ---")
print(f"Minutos: 14 | 3PT Tentados: 3 | Rebotes: 5")
print(f"Pontuação Estimada: {predicao[0]:.1f} pontos")
