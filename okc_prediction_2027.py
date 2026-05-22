import numpy as np
import pandas as pd

def simulate_okc_season(num_simulations=10000):
    # Dados históricos consolidados da temporada anterior (2025/26)
    games_in_season = 82
    okc_pts_avg = 119.0
    okc_opp_pts_avg = 107.9
    
    # Desvio padrão estimado baseado na variação comum de pontuação da NBA
    okc_sd = 11.5
    opp_sd = 11.5
    
    sim_results = []
    
    for _ in range(num_simulations):
        # Simula a pontuação de todos os 82 jogos usando distribuição normal
        okc_scores = np.random.normal(okc_pts_avg, okc_sd, games_in_season)
        opp_scores = np.random.normal(opp_opp_pts_avg, opp_sd, games_in_season)
        
       