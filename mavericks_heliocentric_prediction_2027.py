import numpy as np
import pandas as pd

def simulate_mavericks_season(num_simulations=10000):
    # Calendário padrão da temporada regular da NBA
    games_in_season = 82
    
    # --- Parâmetros de Desempenho (Dallas Mavericks) ---
    # Dallas possui um ataque de elite impulsionado por isolações e espaçamento,
    # gerando médias altas de pontuação, enquanto a defesa opera em nível competitivo estável.
    mvs_pts_avg = 118.5
    mvs_opp_pts_avg = 113.2
    
    # Desvio padrão calibrado em 11.8 para representar o teto explosivo do ataque
    # (noites com alto volume de bolas de 3) combinada com a dependência do núcleo principal.
    mvs_sd = 11.8
    opp_sd = 11.4
    
    sim_results = []
    
    print("Processando dados e simulando cenários para o Dallas Mavericks...")
    
    for _ in range(num_simulations):
        # Geração de pontuações via distribuição normal para os 82 jogos
        mvs_scores = np.random.normal(mvs_pts_avg, mvs_sd, games_in_season)
        opp_scores = np.random.normal(mvs_opp_pts_avg, opp_sd, games_in_season)
        
        # Computa vitória quando o ataque de Dallas supera a defesa adversária
        wins = np.sum(mvs_scores > opp_scores)
        sim_results.append(wins)
        
    # Análise descritiva da distribuição gerada
    sim_series = pd.Series(sim_results)
    mean_wins = sim_series.mean()
    