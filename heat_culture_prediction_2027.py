import numpy as np
import pandas as pd

def simulate_heat_season(num_simulations=10000):
    # Calendário padrão da temporada regular da NBA
    games_in_season = 82
    
    # --- Parâmetros de Desempenho (Miami Heat) ---
    # Miami dita um ritmo físico e amarra o ataque adversário, 
    # o que mantém as médias de pontos dos dois lados mais baixas.
    heat_pts_avg = 113.8
   