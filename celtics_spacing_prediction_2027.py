import numpy as np
import pandas as pd

def simulate_celtics_season(num_simulations=10000):
    # Calendário regulamentar da NBA
    games_in_season = 82
    
    # --- Parâmetros de Desempenho (Boston Celtics) ---
    # Boston opera com um teto ofensivo altíssimo devido ao volume de bolas de 3 
    # e uma defesa sufocante nas alas, resultando em um Net Rating dominante.
    celtics_pts_avg = 121.2
    celtics_opp_pts_avg = 110.4
    
    