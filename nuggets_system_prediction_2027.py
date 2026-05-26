import numpy as np
import pandas as pd

def simulate_nuggets_season(num_simulations=10000):
    # Calendário regulamentar da NBA
    games_in_season = 82
    
    # --- Parâmetros de Desempenho (Denver Nuggets) ---
    # Denver possui uma alta eficiência ofensiva devido ao QI de jogo de Jokić, 
    # mantendo um saldo positivo consistente (Net Rating de elite).
    nuggets_pts_avg = 117.8
    nuggets_opp_pts_avg = 112.1
    
    