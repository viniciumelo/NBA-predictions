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
    
    # Intervalo de confiança bicaudal de 95%
    ci_lower = sim_series.quantile(0.025)
    ci_upper = sim_series.quantile(0.975)
    
    # Probabilidade de atingir metas competitivas na Conferência Oeste
    prob_45_plus = (sim_series >= 45).mean() * 100         # Vaga direta/Briga no Top 6
    prob_50_plus = (sim_series >= 50).mean() * 100         # Campanha de elite com mando de quadra
    
    print("\n" + "=" * 55)
    print("  PREDIÇÃO DE TEMPORADA REGULAR - PHOENIX SUNS 2026/27  ")
    print("=" * 55)
    print(f"Média de Vitórias Projetada: {mean_wins:.1f} - {games_in_season - mean_wins:.1f}")
    print(f"Mediana de Vitórias:          {median_wins:.0f}")
    print(f"Moda mais frequente:         {mode_wins:.0f}")
    print(f"Intervalo de Confiança (95%): {ci_lower:.0f} a {ci_upper:.0f} vitórias")
    