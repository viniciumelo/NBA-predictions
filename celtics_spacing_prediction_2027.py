import numpy as np
import pandas as pd

def simulate_celtics_season(num_simulations=10000):
    # Calendário regulamentar da NBA
    games_in_season = 82
    
    # --- Parâmetros de Desempenho (Boston Celtics) ---
    # Boston opera com um teto ofensivo altíssimo devido ao volume de bolas de 3 
    # e uma defesa sufocante nas alas, resultando em um Net Rating dominante.
    celtics_pts_avg = 121.2
    celtics_opp_pts_avg = 110.4
    
    # Desvio padrão baixo (10.2) para refletir a consistência do sistema.
    # Como o ataque não depende de um único jogador (Jayson Tatum e Jaylen Brown dividem a carga),
    # o time mantém o padrão de vitórias mesmo com desfalques pontuais.
    celtics_sd = 10.2
    opp_sd = 10.8
    
    sim_results = []
    
    print("Processando dados e simulando cenários para o Boston Celtics...")
    
    for _ in range(num_simulations):
        # Geração de pontuações via distribuição normal para os 82 jogos
        celtics_scores = np.random.normal(celtics_pts_avg, celtics_sd, games_in_season)
        opp_scores = np.random.normal(celtics_opp_pts_avg, opp_sd, games_in_season)
        
        # Computa vitória quando o ataque de Boston supera a defesa adversária
        wins = np.sum(celtics_scores > opp_scores)
        sim_results.append(wins)
        
  