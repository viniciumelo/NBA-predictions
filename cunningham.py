import pandas as pd
import numpy as np
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler

# 1. Dados Reais de Fevereiro de 2026 (Detroit Pistons)
# Cade tem tido jogos de alto volume de arremessos (20+)
data = {
    'minutos': [34, 38, 32, 36, 35, 37, 30],
    'usage_rate': [28.5, 33.1, 26.0, 31.4, 30.2, 34.0, 25.5],
    'pontos': [22, 31, 19, 26, 25, 34, 18]
}

df = pd.DataFrame(data)

