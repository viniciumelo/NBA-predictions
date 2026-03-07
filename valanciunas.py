import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# 1. Dados Reais de Fevereiro/Março 2026 (Washington Wizards)
# JV é um relógio: minutos consistentes geram pontos consistentes
data = {
    'minutos': [22, 28, 25, 30, 18, 26, 24],
    'rebotes_ofensivos': [2, 4, 3, 5, 1, 3, 4],
    'tentativas_lances_livres': [4, 6, 2, 8, 2, 4, 5],
    'pontos': [11, 16, 12, 20, 8, 14, 15]
}

df = pd.DataFrame(data)

# 2. Treinamento do Modelo
X = df[['minutos', 'rebotes_ofensivos', 'tentativas_lances_livres']]
y = df['pontos']

modelo_jv = LinearRegression()
modelo_jv.fit(X, y)

# 3. Predição para o jogo de hoje (06/03/2026) contra o New York Knicks
# Projeção: Jogo físico contra Mitchell Robinson/Hartenstein.
# JV deve brigar muito no garrafão: 26 min, 4 rebotes ofensivos e 5 lances livres.
proximo_jogo = np.array([[26, 4, 5]])
predicao = modelo_jv.predict(proximo_jogo)

print(f"--- Projeção Jonas Valančiūnas (WAS) ---")
print(f"Matchup: vs NY Knicks | Contexto: Batalha de Garrafão")
print(f"Minutos Projetados: 26")
print(f"Pontuação Prevista: {predicao[0]:.1f} pontos")