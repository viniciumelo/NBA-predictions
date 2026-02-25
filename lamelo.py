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

# SVR com kernel RBF para capturar relações não-lineares
modelo_lamelo = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=0.1)
modelo_lamelo.fit(X_scaled, y)

# 3. Predição para o próximo jogo contra o Indiana Pacers (26/02/2026)
# Projeção: Jogo de alta velocidade, ~30 min e ele deve converter umas 4 bolas de 3
proximo_jogo = np.array([[30, 4]])
proximo_jogo_scaled = scaler.transform(proximo_jogo)
predicao = modelo_lamelo.predict(proximo_jogo_scaled)

print(f"--- Projeção LaMelo Ball ---")
print(f"Cenário: Jogo vs Pacers | Minutos: 30")
print(f"Bolas de 3 esperadas: 4")
print(f"Pontuação Prevista: {predicao[0]:.1f} pontos")