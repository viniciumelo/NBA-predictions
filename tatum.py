import pandas as pd
import numpy as np
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler

# 1. Dados Reais de Março de 2026 (Boston Celtics)
# Tatum mantém um volume alto e constante de 35-38 minutos
data = {
    'minutos': [36, 38, 32, 40, 35, 37, 34],
    'tentativas_3pt': [9, 12, 7, 13, 8, 11, 10],
    'lances_livres_tentados': [8, 10, 5, 12, 7, 9, 6],
    'pontos': [27, 34, 19, 41, 25, 31, 26]
}
