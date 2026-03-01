import pandas as pd
import numpy as np
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler

# 1. Dados Reais de Fevereiro/Março 2026 (Minnesota Timberwolves)
# Note que quando ele tenta mais de 20 arremessos, a pontuação decola
data = {
    'minutos': [35, 38, 32, 36, 40, 34, 37],
    'tentativas_fg': [18, 24, 15, 21, 26, 19, 22],
    'lances_livres': [6, 9, 4, 8, 12, 5, 7],
    'pontos': [26, 34, 19, 31, 42, 24, 33]
}

df = pd.DataFrame(data)

# 2. Preparação dos Dados
X = df[['minutos', 'tentativas_fg', 'lances_livres']]
y = df['pontos']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Treinamento do Modelo SGD (Sensível ao ímpeto ofensivo)
modelo_ant = SGDRegressor(max_iter=1000, tol=1e-3, random_state=42)
modelo_ant.fit(X_scaled, y)

# 4. Predição para o próximo jogo contra o Phoenix Suns (03/03/2026)
# Projeção: Jogo de alto nível, 37 min, 22 arremessos e 8 lances livres
proximo_jogo = np.array([[37, 22, 8]])
proximo_jogo_scaled = scaler.transform(proximo_jogo)
predicao = modelo_ant.predict(proximo_jogo_scaled)

print(f"--- Projeção Anthony Edwards ---")
print(f"Status: Candidato a MVP | Minutos: 37")
print(f"Volume Estimado: 22 FG / 8 FT")
print(f"Pontuação Prevista: {predicao[0]:.1f} pontos")