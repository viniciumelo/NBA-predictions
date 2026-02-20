import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# 1. Dados Reais (Temporada 2025-26 - Logs de Janeiro/Fevereiro)
# Giannis tem um "piso" de pontos muito alto devido aos lances livres
data = {
    'minutos': [32, 31, 30, 22, 31, 34, 35, 29],
    'lances_livres_tentados': [16, 6, 12, 9, 14, 15, 13, 11],
    'pontos': [22, 19, 21, 21, 25, 33, 31, 28]
}

df = pd.DataFrame(data)

