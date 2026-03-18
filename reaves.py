import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge

# Dados recentes de Austin Reaves (Março 2026)
data = {
    'game': [1, 2, 3, 4, 5, 6],
    'pts': [19, 25, 31, 30, 32, 15], # Sequência: IND, NYK, MIN, CHI, DEN, HOU
    'min': [29, 39, 38, 39, 46, 40],
    'opp_def_rank': [15, 5, 2, 20, 10, 8] # Ranking defensivo fictício dos oponentes
}
