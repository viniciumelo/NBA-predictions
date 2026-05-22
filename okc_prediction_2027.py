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
        
        # Calcula as vitórias (onde a pontuação do OKC foi maior)
        wins = np.sum(okc_scores > opp_scores)
        sim_results.append(wins)
        
    # Processa os resultados estatísticos da simulação
    sim_series = pd.Series(sim_results)
    mean_wins = sim_series.mean()
    median_wins = sim_series.median()
    mode_wins = sim_series.mode()[0]
    
    # Intervalo de confiança de 95% (percentis 2.5 e 97.5)
    ci_lower = sim_series.quantile(0.025)
    ci_upper = sim_series.quantile(0.975)
    
    