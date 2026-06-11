import numpy as np
import pandas as pd

def simulate_hornets_season(num_simulations=10000):
    # Calendário padrão da temporada regular da NBA
    games_in_season = 82
    
    # --- Parâmetros de Desempenho (Charlotte Hornets) ---
    # Hornets operam em ritmo acelerado, gerando boas médias de ataque,
    # enquanto buscam consolidação e consistência no sistema defensivo.
    hornets_pts_avg = 114.2
    hornets_opp_pts_avg = 117.5
    
    # Desvio padrão calibrado em 12.0 para representar a volatilidade natural
    # de equipes velozes de transição, suscetíveis a sequências de rachas de pontos.
    hornets_sd = 12.0
   