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
    opp_sd = 11.6
    
   sim_results = []
    
    print("Processando dados e simulando cenários para o Charlotte Hornets...")
    
    for _ in range(num_simulations):
        # Geração de pontuações via distribuição normal para os 82 jogos
        hornets_scores = np.random.normal(hornets_pts_avg, hornets_sd, games_in_season)
        opp_scores = np.random.normal(hornets_opp_pts_avg, opp_sd, games_in_season)
        
        # Computa vitória quando o ataque de Charlotte supera a defesa adversária
        wins = np.sum(hornets_scores > opp_scores)
        sim_results.append(wins)
        
    