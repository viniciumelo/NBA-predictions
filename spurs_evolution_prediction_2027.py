import numpy as np
import pandas as pd

def simulate_spurs_season(num_simulations=10000):
    # Calendário padrão da temporada regular da NBA
    games_in_season = 82
    
    # --- Parâmetros de Projeção (Fator de Evolução) ---
    # Modelamos um incremento na média de pontos feitos e uma redução nos pontos sofridos,
    # refletindo o impacto defensivo gerado pelo amadurecimento do Wemby na área pintada.
    spurs_pts_avg = 114.8
    spurs_opp_pts_avg = 111.2
    
    # Desvio padrão ligeiramente maior (12.2) para representar a volatilidade natural 
    # de elencos jovens (picos de grande desempenho misturados com oscilações de experiência)
    spurs_sd = 12.2
    opp_sd = 11.8
    
    sim_results = []
    
    print("Executando simulações para a temporada do San Antonio Spurs...")
    
    for _ in range(num_simulations):
        # Geração de pontuações baseada em distribuição normal para os 82 confrontos
        spurs_scores = np.random.normal(spurs_pts_avg, spurs_sd, games_in_season)
        opp_scores = np.random.normal(spurs_opp_pts_avg, opp_sd, games_in_season)
        
        # Computa vitória quando o ataque supera a defesa adversária
        wins = np.sum(spurs_scores > opp_scores)
        sim_results.append(wins)
        
    # Agrupamento e análise dos dados simulados
    sim_series = pd.Series(sim_results)
    mean_wins = sim_series.mean()
    median_wins = sim_series.median()
    mode_wins = sim_series.mode()[0]
    
    # Intervalo de confiança bicaudal de 95%
    ci_lower = sim_series.quantile(0.025)
    ci_upper = sim_series.quantile(0.975)
    
    