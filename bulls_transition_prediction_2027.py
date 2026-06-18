import numpy as np
import pandas as pd

def simulate_bulls_season(num_simulations=10000):
    # Calendário regulamentar da NBA
    games_in_season = 82
    
    # --- Parâmetros de Desempenho (Chicago Bulls) ---
    # Os Bulls sustentam um bom volume de pontos atacando em transição rápida,
    # enquanto trabalham para consolidar os ajustes na rotação defensiva de perímetro.
    bulls_pts_avg = 114.5
    bulls_opp_pts_avg = 117.2
    
    # Desvio padrão calibrado em 11.9 para representar a volatilidade natural
    # de times que jogam em ritmo veloz e dependem do aproveitamento de arremessos externos.
    bulls_sd = 11.9
    opp_sd = 11.5

    sim_results = []
    
    print("Processando dados e simulando cenários para o Chicago Bulls...")
    
    for _ in range(num_simulations):
        # Geração de pontuações via distribuição normal para os 82 jogos
        bulls_scores = np.random.normal(bulls_pts_avg, bulls_sd, games_in_season)
        opp_scores = np.random.normal(bulls_opp_pts_avg, opp_sd, games_in_season)
        
        # Computa vitória quando o ataque de Chicago supera a defesa adversária
        wins = np.sum(bulls_scores > opp_scores)
        sim_results.append(wins)
        
    # Análise descritiva da distribuição gerada
    sim_series = pd.Series(sim_results)
    mean_wins = sim_series.mean()
    