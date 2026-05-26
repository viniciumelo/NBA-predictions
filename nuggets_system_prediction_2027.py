import numpy as np
import pandas as pd

def simulate_nuggets_season(num_simulations=10000):
    # Calendário regulamentar da NBA
    games_in_season = 82
    
    # --- Parâmetros de Desempenho (Denver Nuggets) ---
    # Denver possui uma alta eficiência ofensiva devido ao QI de jogo de Jokić, 
    # mantendo um saldo positivo consistente (Net Rating de elite).
    nuggets_pts_avg = 117.8
    nuggets_opp_pts_avg = 112.1
    
    # Desvio padrão calibrado em 11.0. 
    # O time titular é muito estável, mas a rotação do banco introduz uma variação moderada.
    nuggets_sd = 11.0
    opp_sd = 11.4
    
    sim_results = []
    
    print("Calculando projeções probabilísticas para o Denver Nuggets...")
    
    for _ in range(num_simulations):
        # Simulação por amostragem de distribuição normal para os 82 jogos
        nuggets_scores = np.random.normal(nuggets_pts_avg, nuggets_sd, games_in_season)
        opp_scores = np.random.normal(nuggets_opp_pts_avg, opp_sd, games_in_season)
        
       