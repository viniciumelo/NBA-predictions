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

