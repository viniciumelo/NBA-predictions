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
    
    sim_results = []
    
    print("Processando dados e simulando cenários para o Phoenix Suns...")
    
    for _ in range(num_simulations):
        # Geração de pontuações via distribuição normal para os 82 jogos
        suns_scores = np.random.normal(suns_pts_avg, suns_sd, games_in_season)
        opp_scores = np.random.normal(suns_opp_pts_avg, opp_sd, games_in_season)
        
        # Computa vitória quando o ataque de Phoenix supera a defesa adversária
        wins = np.sum(suns_scores > opp_scores)
        sim_results.append(wins)
        
    # Análise descritiva da distribuição gerada
    sim_series = pd.Series(sim_results)
    mean_wins = sim_series.mean()
    median_wins = sim_series.median()
    mode_wins = sim_series.mode()[0]
    
    