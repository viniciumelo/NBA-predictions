import numpy as np
import pandas as pd

def simulate_timberwolves_season(num_simulations=10000):
    # Calendário padrão da temporada regular da NBA
    games_in_season = 82
    
    # --- Parâmetros de Desempenho (Minnesota Timberwolves) ---
    # Minnesota se destaca por travar o ataque adversário com uma defesa sufocante,
    # gerando um dos melhores ratings defensivos da liga e vencendo pelo equilíbrio lá atrás.
    twolves_pts_avg = 116.5
    twolves_opp_pts_avg = 110.2
    
    # Desvio padrão calibrado em 11.0 para representar um sistema defensivo sólido,
    # que garante estabilidade e regularidade durante os 82 jogos da temporada.
    twolves_sd = 11.0
    opp_sd = 11.4
    
    