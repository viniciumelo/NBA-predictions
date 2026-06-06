import numpy as np
import pandas as pd

def simulate_timberwolves_season(num_simulations=10000):
    # Calendário padrão da temporada regular da NBA
    games_in_season = 82
    
    # --- Parâmetros de Desempenho (Minnesota Timberwolves) ---
    # Minnesota se destaca por travar o ataque adversário com uma defesa sufocante,
    # gerando um dos melhores ratings defensivos da liga e vencendo pelo equilíbrio lá atrás.
    twolves_pts_avg = 116.5
    twolves_opp_pts_avg = 110.2
    
    # Desvio padrão calibrado em 11.0 para representar um sistema defensivo sólido,
    # que garante estabilidade e regularidade durante os 82 jogos da temporada.
    twolves_sd = 11.0
    opp_sd = 11.4
    
    sim_results = []
    
    print("Processando dados e simulando cenários para o Minnesota Timberwolves...")
    
    for _ in range(num_simulations):
        # Geração de pontuações via distribuição normal para os 82 jogos
        twolves_scores = np.random.normal(twolves_pts_avg, twolves_sd, games_in_season)
        opp_scores = np.random.normal(twolves_opp_pts_avg, opp_sd, games_in_season)
        
        # Computa vitória quando o ataque de Minnesota supera a defesa adversária
        wins = np.sum(twolves_scores > opp_scores)
        sim_results.append(wins)
        
    # Análise descritiva da distribuição gerada
    sim_series = pd.Series(sim_results)
    mean_wins = sim_series.mean()
    median_wins = sim_series.median()
    mode_wins = sim_series.mode()[0]
    
    # Intervalo de confiança bicaudal de 95%
    ci_lower = sim_series.quantile(0.025)
    ci_upper = sim_series.quantile(0.975)
    
    # Probabilidade de atingir marcas de elite na disputada Conferência Oeste
    prob_50_plus = (sim_series >= 50).mean() * 100         # Mando de quadra garantido nos Playoffs
    