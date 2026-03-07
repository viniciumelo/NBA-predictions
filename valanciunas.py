import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# 1. Dados Reais de Fevereiro/Março 2026 (Washington Wizards)
# JV é um relógio: minutos consistentes geram pontos consistentes
data = {
    'minutos': [22, 28, 25, 30, 18, 26, 24],
    'rebotes_ofensivos': [2, 4, 3, 5, 1, 3, 4],
    'tentativas_lances_livres': [4, 6, 2, 8, 2, 4, 5],
    'pontos': [11, 16, 12, 20, 8, 14, 15]
}

df = pd.DataFrame(data)

