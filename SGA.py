import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 1. Dados reais simplificados do SGA (Temporada 2025-26)
# Simulando logs de jogos recentes (Minutos vs Pontos)
data = {
    'minutos': [28, 33, 31, 36, 35, 38, 34, 32],
    'pontos': [20, 34, 30, 29, 24, 37, 31, 28]
}

df = pd.DataFrame(data)

# 2. Preparação do Modelo
X = df[['minutos']] # Variável independente
y = df['pontos']    # Variável alvo (o que queremos prever)

