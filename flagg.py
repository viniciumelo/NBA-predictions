import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor

# 1. Dados Reais de Fevereiro de 2026 (Mavericks)
# Flagg teve uma explosão de pontos antes da lesão
data = {
    'minutos': [37, 39, 36, 36, 28, 34, 31],
    'tentativas_fg': [24, 27, 20, 16, 12, 15, 14],
    'pontos': [36, 32, 27, 20, 14, 23, 18]
}

df = pd.DataFrame(data)

# 2. Modelo KNN (Busca padrões em jogos com minutagem parecida)
X = df[['minutos', 'tentativas_fg']]
y = df['pontos']

