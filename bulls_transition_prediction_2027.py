import numpy as np
import pandas as pd

def simulate_bulls_season(num_simulations=10000):
    # Calendário regulamentar da NBA
    games_in_season = 82
    
    # --- Parâmetros de Desempenho (Chicago Bulls) ---
    # Os Bulls sustentam um bom volume de pontos atacando em transição rápida,
    # enquanto trabalham para consolidar os ajustes na rotação defensiva de perímetro.
    bulls_pts_avg = 114.5
    