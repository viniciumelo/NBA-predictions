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

