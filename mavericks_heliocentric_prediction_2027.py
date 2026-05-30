import numpy as np
import pandas as pd

def simulate_mavericks_season(num_simulations=10000):
    # Calendário padrão da temporada regular da NBA
    games_in_season = 82
    
    # --- Parâmetros de Desempenho (Dallas Mavericks) ---
    # Dallas possui um ataque de elite impulsionado por isolações e espaçamento,
    # gerando médias altas de pontuação, enquanto a defesa opera em nível competitivo estável.
    mvs_pts_avg = 118.5
    mvs_opp_pts_avg = 113.2
    
    