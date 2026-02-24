import pandas as pd
import numpy as np
from sklearn.linear_model import Lasso

# 1. Dados Reais de Fevereiro de 2026 (Utah Jazz)
# Love oscila dependendo do matchup (se o adversário tem pivôs lentos)
data = {
    'minutos': [16, 12, 15, 24, 13, 21, 18],
    'tentativas_3pt': [5, 3, 3, 4, 1, 3, 5],
    'rebotes_totais': [9, 6, 5, 11, 4, 11, 3],
    'pontos': [5, 13, 4, 3, 5, 6, 11]
}

df = pd.DataFrame(data)

