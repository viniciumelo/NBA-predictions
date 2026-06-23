import numpy as np
import pandas as pd

def simulate_magic_season(num_simulations=10000):
    # Calendário regulamentar da NBA
    games_in_season = 82
    
    # --- Parâmetros de Desempenho (Orlando Magic) ---
    # Orlando dita o ritmo através de uma defesa sufocante, mantendo a média 
    # de pontos dos adversários em patamares baixos, compensando um ataque focado em meia-quadra.
    magic_pts_avg = 114.8
    