import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge

# 1. Dados Reais de Março de 2026 (OKC Thunder)
# A pontuação do Hartenstein é estável, raramente passando dos 15 ou caindo abaixo de 4.
data = {
    'minutos': [28, 32, 25, 30, 26, 29, 31],
    'rebotes_ofensivos': [3, 5, 2, 4, 3, 4, 5],
    'assistencias': [5, 4, 3, 6, 2, 5, 4],
    'pontos': [8, 12, 6, 10, 7, 9, 11]
}

df = pd.DataFrame(data)

# 2. Treinamento do Modelo Ridge (Regularizado para evitar distorções)
X = df[['minutos', 'rebotes_ofensivos', 'assistencias']]
y = df['pontos']

modelo_ih = Ridge(alpha=0.5)
modelo_ih.fit(X, y)

# 3. Predição para o próximo jogo (10/03/2026) contra o New Orleans Pelicans
# Projeção: Jogo físico contra Zion/JV. 
# Hartenstein deve jogar ~29 min, pegar 4 rebotes ofensivos e distribuir 4 assistências.
proximo_jogo = np.array([[29, 4, 4]])
predicao = modelo_ih.predict(proximo_jogo)

print(f"--- Projeção Isaiah Hartenstein (OKC) ---")
print(f"Data: 10 de Março de 2026 | Função: Pivô Facilitador")
print(f"Minutos Projetados: 29")
print(f"Pontuação Estimada: {predicao[0]:.1f} pontos")