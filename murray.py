import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# 1. Dados Reais (Temporada 2025-26 - Fevereiro)
# Incluímos o 'outlier' de ontem para o modelo entender a volatilidade
data = {
    'jogo_id': [1, 2, 3, 4, 5, 6, 7],
    'minutos': [31, 48, 36, 34, 33, 25, 8], # Jogo 7 foi a saída precoce por doença
    '3pt_tentados': [9, 14, 6, 5, 6, 12, 2],
    'pontos': [28, 39, 17, 20, 21, 25, 2] 
}

df = pd.DataFrame(data)

# 2. Modelo de Pesos (Dando menos peso ao jogo de doença/lesão)
# Pesos: 1.0 para jogos normais, 0.1 para o jogo atípico de ontem
pesos = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.1]

X = df[['minutos', '3pt_tentados']]
y = df['pontos']

modelo_murray = LinearRegression()
modelo_murray.fit(X, y, sample_weight=pesos)

