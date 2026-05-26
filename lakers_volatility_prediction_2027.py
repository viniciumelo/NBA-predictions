import numpy as np
import pandas as pd

def simulate_lakers_season(num_simulations=10000):
    # Calendário regulamentar da NBA
    games_in_season = 82
    
    # --- Parâmetros de Desempenho (LA Lakers) ---
    # Os Lakers mantêm um ataque forte focado na infiltração e garrafão,
    # mas operam com um saldo de pontos mais equilibrado na temporada regular.
    lakers_pts_avg = 116.4
    lakers_opp_pts_avg = 113.8
    