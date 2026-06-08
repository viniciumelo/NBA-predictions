import numpy as np
import pandas as pd

def simulate_blazers_season(num_simulations=10000):
    # Calendário padrão da temporada regular da NBA
    games_in_season = 82
    
    # --- Parâmetros de Desempenho (Portland Trail Blazers) ---
    # Como uma equipe jovem em desenvolvimento, as médias projetadas refletem
    # um ataque veloz e talentoso, mas que ainda cede pontos devido a ajustes defensivos.
    blazers_pts_avg = 111.4
    blazers_opp_pts_avg = 117.8
    
    # Desvio padrão calibrado em 12.4 para representar a alta volatilidade.
    # Times jovens podem surpreender candidatos ao título em noites inspiradas,
    # mas também oscilar bastante em sequências de jogos fora de casa (road trips).
    blazers_sd = 12.4
   