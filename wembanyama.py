import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# 1. Dados Reais de Fevereiro de 2026 (Logs de Jogos)
# Wemby oscila minutos devido a placares elásticos (blowouts)
data = {
    'minutos': [33, 26, 27, 34, 28, 27, 30, 28],
    'tentativas_3pts': [9, 6, 6, 9, 2, 4, 3, 3],
    'pontos': [26, 40, 16, 29, 22, 25, 16, 28]
}

df = pd.DataFrame(data)

