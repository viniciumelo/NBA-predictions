import numpy as np
import pandas as pd

def simulate_knicks_season(num_simulations=10000):
    # Número de jogos na temporada regular da NBA
    games_in_season = 82
    
    # Parâmetros de desempenho baseados na identidade competitiva dos Knicks
    # Média de pontos feitos e sofridos estimada a partir do ritmo controlado (Pace)
    knicks_pts_avg = 115.5
    knicks_opp_pts_avg = 109.2
    