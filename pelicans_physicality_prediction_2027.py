import numpy as np
import pandas as pd

def simulate_pelicans_season(num_simulations=10000):
    # Calendário padrão da temporada regular da NBA
    games_in_season = 82
    
    # --- Parâmetros de Desempenho (New Orleans Pelicans) ---
    # New Orleans apresenta um ataque eficiente punindo o garrafão adversário,
    # mantendo um saldo positivo seguro quando a rotação principal está saudável.
    pelicans_pts_avg = 116.8
    pelicans_opp_pts_avg = 113.2
    
    # Desvio padrão elevado para 12.5.
    # Reflete a volatilidade natural gerada por fatores de gerenciamento de carga,
    # desgaste físico ao longo de 82 jogos e mudanças pontuais no quinteto titular.
    pelicans_sd = 12.5
    opp_sd = 11.9

    sim_results = []
    
    print("Processando dados e simulando cenários para o New Orleans Pelicans...")
    
    for _ in range(num_simulations):
        # Geração de pontuações via distribuição normal para os 82 jogos
        pelicans_scores = np.random.normal(pelicans_pts_avg, pelicans_sd, games_in_season)
        opp_scores = np.random.normal(pelicans_opp_pts_avg, opp_sd, games_in_season)
        
        # Computa vitória quando o ataque de New Orleans supera a defesa adversária
        wins = np.sum(pelicans_scores > opp_scores)
        sim_results.append(wins)
        
    # Análise descritiva da distribuição gerada
    sim_series = pd.Series(sim_results)
    mean_wins = sim_series.mean()
    median_wins = sim_series.median()
    mode_wins = sim_series.mode()[0]

    # Intervalo de confiança bicaudal de 95%
    ci_lower = sim_series.quantile(0.025)
    