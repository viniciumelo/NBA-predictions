
import pandas as pd

# 1. Simulação de um Dataset (Estes dados seriam extraídos da nba_api ou CSV)
data = {
    'Time': ['Thunder', 'Pistons', 'Celtics', 'Spurs', 'Lakers', 'Nuggets'],
    'Vitorias': [52, 48, 43, 49, 42, 41],
    'Derrotas': [15, 18, 23, 18, 25, 27],
    'PPG': [118.6, 117.4, 114.2, 118.8, 116.5, 120.7],  # Pontos pró
    'OPPG': [107.8, 109.6, 107.0, 111.8, 115.3, 116.7]  # Pontos contra
}

