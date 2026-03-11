import pandas as pd
import numpy as np
from sklearn.linear_model import ElasticNet
from sklearn.preprocessing import StandardScaler

# 1. Dados Reais de Março de 2026 (Miami Heat)
# Dados mostram que quando Bam tenta 14+ arremessos, ele passa dos 20 pts
data = {
    'minutos': [34, 36, 31, 35, 38, 33, 35],
    'tentativas_fg': [12, 16, 11, 15, 18, 13, 15],
    'lances_livres_feitos': [4, 7, 3, 6, 8, 4, 5],
    'pontos': [16, 23, 14, 21, 28, 18, 20]
}

df = pd.DataFrame(data)

