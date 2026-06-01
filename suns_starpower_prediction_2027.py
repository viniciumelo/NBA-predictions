import numpy as np
import pandas as pd

def simulate_suns_season(num_simulations=10000):
    # Calendário padrão da temporada regular da NBA
    games_in_season = 82
    
    # --- Parâmetros de Desempenho (Phoenix Suns) ---
    # Phoenix opera com alta eficiência ofensiva focada em arremessos de elite,
    # mantendo uma média de pontuação robusta e uma defesa competitiva.
    suns_pts_avg = 117.2
    suns_opp_pts_avg = 113.5
    
    # Desvio padrão calibrado em 12.1 para representar a variância de times 
    # dependentes de arremessos de meia-distância e perímetro, além do fator desgaste.
    suns_sd = 12.1
    opp_sd = 11.6
    
   x