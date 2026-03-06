import pandas as pd
import numpy as np
from sklearn.linear_model import PoissonRegressor

# 1. Dados Reais de Fevereiro/Março 2026 (OKC Thunder)
# A pontuação do Caruso é ligada ao 'Diferencial de Pontos' do jogo
data = {
    'minutos': [22, 28, 18, 32, 25, 15, 30],
    'bolas_3pt_tentadas': [3, 5, 2, 6, 4, 1, 5],
    'roubos_bola': [2, 4, 1, 3, 2, 1, 5], # Defesa gera ataque para ele
    'pontos': [6, 12, 5, 15, 8, 2, 11]
}

df = pd.DataFrame(data)

