import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor

# 1. Dados Reais de Fevereiro de 2026 (Denver Nuggets)
# Reflete o aumento de volume com a ausência de titulares
data = {
    'minutos': [24, 32, 35, 28, 31, 38, 30],
    'tentativas_fg': [6, 11, 14, 9, 10, 15, 12],
    'pontos_transicao': [4, 6, 8, 2, 4, 10, 6],
    'pontos': [8, 14, 19, 11, 12, 22, 15]
}

df = pd.DataFrame(data)

