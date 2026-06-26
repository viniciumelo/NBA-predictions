import numpy as np
import pandas as pd

def simulate_bucks_season(num_simulations=10000):
    # Calendário regulamentar da NBA
    games_in_season = 82
    
    # --- Parâmetros de Desempenho (Milwaukee Bucks) ---
    # Milwaukee mantém um teto ofensivo muito forte devido à eficiência na área pintada
    # e volume de arremessos, operando com um sólido diferencial positivo.
    bucks_pts_avg = 118.2
    