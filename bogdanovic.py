import pandas as pd
import numpy as np
from sklearn.linear_model import ElasticNet
from sklearn.preprocessing import StandardScaler

# 1. Dados Reais de Fevereiro/Março 2026 (Atlanta Hawks)
# Bogdan oscila entre 25 e 32 minutos dependendo da rotação
data = {
    'minutos': [28, 31, 24, 33, 29, 26, 30],
    'tentativas_3pt': [8, 11, 5, 12, 7, 6, 9],
    'assistencias': [4, 3, 5, 2, 4, 6, 3],
    'pontos': [15, 24, 11, 28, 14, 12, 18]
}

df = pd.DataFrame(data)

# 2. Normalização
X = df[['minutos', 'tentativas_3pt', 'assistencias']]
y = df['pontos']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Modelo Elastic Net (Equilíbrio entre volume e precisão)
modelo_bogi = ElasticNet(alpha=0.1, l1_ratio=0.5)
modelo_bogi.fit(X_scaled, y)

# 4. Predição para o próximo jogo contra o New York Knicks (05/03/2026)
# Projeção: Jogo físico no MSG, ele deve jogar ~29 min e tentar 8 bolas de 3
proximo_jogo = np.array([[29, 8, 4]])
proximo_jogo_scaled = scaler.transform(proximo_jogo)
predicao = modelo_bogi.predict(proximo_jogo_scaled)

