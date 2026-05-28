import numpy as np
import pandas as pd

def simulate_cavaliers_season(num_simulations=10000):
    # Calendário padrão da temporada regular da NBA
    games_in_season = 82
    
    # --- Parâmetros de Desempenho (Cleveland Cavaliers) ---
    # Cleveland baseia seu jogo em uma das melhores defesas de garrafão da liga,
    # segurando os adversários abaixo de médias elásticas de pontuação.
    cavs_pts_avg = 115.8
    cavs_opp_pts_avg = 110.2
    
    # Desvio padrão calibrado em 10.9 para representar a previsibilidade defensiva,
    # balanceando oscilações pontuais no aproveitamento do perímetro.
    cavs_sd = 10.9
    opp_sd = 11.3
    
    sim_results = []
    
    print("Processando dados e simulando cenários para o Cleveland Cavaliers...")
    
    for _ in range(num_simulations):
        # Geração de pontuações via distribuição normal para os 82 jogos
        cavs_scores = np.random.normal(cavs_pts_avg, cavs_sd, games_in_season)
        opp_scores = np.random.normal(cavs_opp_pts_avg, opp_sd, games_in_season)
        
        # Computa vitória quando o ataque de Cleveland supera a defesa adversária
        wins = np.sum(cavs_scores > opp_scores)
        sim_results.append(wins)
        
    