import numpy as np
import pandas as pd

def simulate_knicks_season(num_simulations=10000):
    # Número de jogos na temporada regular da NBA
    games_in_season = 82
    
    # Parâmetros de desempenho baseados na identidade competitiva dos Knicks
    # Média de pontos feitos e sofridos estimada a partir do ritmo controlado (Pace)
    knicks_pts_avg = 115.5
    knicks_opp_pts_avg = 109.2
    
    # Desvio padrão para simular a volatilidade de jogos da NBA (lesões, back-to-backs, etc.)
    # Knicks costumam ser um time resiliente e de menor oscilação devido ao sistema rígido
    knicks_sd = 10.8
    opp_sd = 11.2
    
    sim_results = []
    
    print("Iniciando Simulação de Monte Carlo para os Knicks...")
    
    for _ in range(num_simulations):
        # Simulação estatística baseada em distribuição normal para os 82 jogos
        knicks_scores = np.random.normal(knicks_pts_avg, knicks_sd, games_in_season)
        opp_scores = np.random.normal(knicks_opp_pts_avg, opp_sd, games_in_season)
        
        # Vitória se os Knicks pontuarem mais que o adversário
        wins = np.sum(knicks_scores > opp_scores)
        sim_results.append(wins)
        
    # Análise de dados dos resultados gerados
    sim_series = pd.Series(sim_results)
    mean_wins = sim_series.mean()
    median_wins = sim_series.median()
    mode_wins = sim_series.mode()[0]
    
    