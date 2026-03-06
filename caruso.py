import pandas as pd
import numpy as np
from sklearn.linear_model import PoissonRegressor

# 1. Dados Reais de Fevereiro/Março 2026 (OKC Thunder)
# A pontuação do Caruso é ligada ao 'Diferencial de Pontos' do jogo
data = {
    'minutos': [22, 28, 18, 32, 25, 15, 30],
    'bolas_3pt_tentadas': [3, 5, 2, 6, 4, 1, 5],
    'roubos_bola': [2, 4, 1, 3, 2, 1, 5], # Defesa gera ataque para ele
    'pontos': [6, 12, 5, 15, 8, 2, 11]
}

df = pd.DataFrame(data)

# 2. Treinamento do Modelo Poisson
X = df[['minutos', 'bolas_3pt_tentadas', 'roubos_bola']]
y = df['pontos']

modelo_caruso = PoissonRegressor(alpha=0.1)
modelo_caruso.fit(X, y)

# 3. Predição para o jogo de amanhã (07/03/2026) contra o Dallas Mavericks
# Projeção: Jogo de alta intensidade (Playoff feel), Caruso deve jogar ~28 min
# e terá que marcar Luka/Kyrie, o que gera roubos e contra-ataques.
proximo_jogo = np.array([[28, 4, 3]])
predicao = modelo_caruso.predict(proximo_jogo)

print(f"--- Projeção Alex Caruso (OKC) ---")
print(f"Matchup: vs Dallas Mavericks | Função: Defensive Stopper")
print(f"Minutos Projetados: 28")
print(f"Pontuação Prevista: {predicao[0]:.1f} pontos")