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
    opp_sd = 11.9
    
   sim_results = []
    
    print("Processando dados e simulando cenários para o Portland Trail Blazers...")
    
    for _ in range(num_simulations):
        # Geração de pontuações via distribuição normal para os 82 jogos
        blazers_scores = np.random.normal(blazers_pts_avg, blazers_sd, games_in_season)
        opp_scores = np.random.normal(blazers_opp_pts_avg, opp_sd, games_in_season)
        
        # Computa vitória quando o ataque de Portland supera a defesa adversária
        wins = np.sum(blazers_scores > opp_scores)
        sim_results.append(wins)
        
    # Análise descritiva da distribuição gerada
    sim_series = pd.Series(sim_results)
    mean_wins = sim_series.mean()
    median_wins = sim_series.median()
    mode_wins = sim_series.mode()[0]
    
    