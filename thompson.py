import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge

# 1. Dados Reais de Fevereiro de 2026 (Logs do Klay no Dallas)
# Note a variação: ele pode fazer 19 pts ou 4 pts dependendo da "mão quente"
data = {
    'minutos': [28, 23, 19, 20, 20, 28, 27],
    'tentativas_3pt': [9, 3, 10, 6, 4, 7, 11],
    'pontos': [11, 9, 19, 5, 4, 9, 16]
}

df = pd.DataFrame(data)

# 2. Modelo Ridge (Estabilidade para arremessadores de volume)
X = df[['minutos', 'tentativas_3pt']]
y = df['pontos']

# Alpha controla a suavização (regularização)
modelo_klay = Ridge(alpha=1.0)
modelo_klay.fit(X, y)

# 3. Predição para o jogo contra o Indiana Pacers (22/02/2026)
# Projeção: Ele deve jogar cerca de 24 minutos e tentar 7 bolas de fora
proximo_jogo = np.array([[24, 7]])
predicao = modelo_klay.predict(proximo_jogo)

print(f"--- Projeção Klay Thompson ---")
print(f"Minutos Projetados: 24 | Volume 3PT: 7")
print(f"Pontuação Estimada: {predicao[0]:.1f} pontos")