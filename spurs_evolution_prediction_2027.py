import numpy as np
import pandas as pd

def simulate_spurs_season(num_simulations=10000):
    # Calendário padrão da temporada regular da NBA
    games_in_season = 82
    
    # --- Parâmetros de Projeção (Fator de Evolução) ---
    # Modelamos um incremento na média de pontos feitos e uma redução nos pontos sofridos,
    # refletindo o impacto defensivo gerado pelo amadurecimento do Wemby na área pintada.
    spurs_pts_avg = 114.8
    spurs_opp_pts_avg = 111.2
    
    