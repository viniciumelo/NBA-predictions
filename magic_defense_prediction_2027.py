import numpy as np
import pandas as pd

def simulate_magic_season(num_simulations=10000):
    # Calendário regulamentar da NBA
    games_in_season = 82
    
    # --- Parâmetros de Desempenho (Orlando Magic) ---
    # Orlando dita o ritmo através de uma defesa sufocante, mantendo a média 
    # de pontos dos adversários em patamares baixos, compensando um ataque focado em meia-quadra.
    magic_pts_avg = 114.8
    magic_opp_pts_avg = 109.5
    
    # Desvio padrão calibrado em 10.7 para representar a previsibilidade da defesa.
    # Como a intensidade defensiva do Magic é consistente e viaja bem (funciona fora de casa),
    # o time sofre menos apagões estatísticos severos.
    magic_sd = 10.7
    opp_sd = 11.1

    sim_results = []
    
    