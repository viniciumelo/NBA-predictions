import numpy as np
import pandas as pd

def simulate_nuggets_season(num_simulations=10000):
    # Calendário regulamentar da NBA
    games_in_season = 82
    
    # --- Parâmetros de Desempenho (Denver Nuggets) ---
    # Denver possui uma alta eficiência ofensiva devido ao QI de jogo de Jokić, 
    # mantendo um saldo positivo consistente (Net Rating de elite).
    nuggets_pts_avg = 117.8
    nuggets_opp_pts_avg = 112.1
    
    # Desvio padrão calibrado em 11.0. 
    # O time titular é muito estável, mas a rotação do banco introduz uma variação moderada.
    nuggets_sd = 11.0
    opp_sd = 11.4
    
    sim_results = []
    
    print("Calculando projeções probabilísticas para o Denver Nuggets...")
    
    for _ in range(num_simulations):
        # Simulação por amostragem de distribuição normal para os 82 jogos
        nuggets_scores = np.random.normal(nuggets_pts_avg, nuggets_sd, games_in_season)
        opp_scores = np.random.normal(nuggets_opp_pts_avg, opp_sd, games_in_season)
        
        # Vitória computada se o ataque de Denver superar a defesa adversária
        wins = np.sum(nuggets_scores > opp_scores)
        sim_results.append(wins)
        
    # Análise descritiva da distribuição gerada
    sim_series = pd.Series(sim_results)
    mean_wins = sim_series.mean()
    median_wins = sim_series.median()
    mode_wins = sim_series.mode()[0]
    
    # Intervalo de confiança bicaudal de 95%
    ci_lower = sim_series.quantile(0.025)
    ci_upper = sim_series.quantile(0.975)
    
    # Probabilidade de atingir metas de mando de quadra no acirrado Oeste
    prob_50_plus = (sim_series >= 50).mean() * 100
    prob_55_plus = (sim_series >= 55).mean() * 100
    
    print("\n" + "=" * 55)
    print("  PREDIÇÃO DE TEMPORADA REGULAR - DENVER NUGGETS 2026/27  ")
    print("=" * 55)
    print(f"Média de Vitórias Projetada: {mean_wins:.1f} - {games_in_season - mean_wins:.1f}")
    print(f"Mediana de Vitórias:          {median_wins:.0f}")
    print(f"Moda mais frequente:         {mode_wins:.0f}")
    print(f"Intervalo de Confiança (95%): {ci_lower:.0f} a {ci_upper:.0f} vitórias")
    print("-" * 55)
    print(f"Probabilidade de vencer 50+ jogos (Mando de Quadra): {prob_50_plus:.2f}%")
    print(f"Probabilidade de vencer 55+ jogos (Elite Contender): {prob_55_plus:.2f}%")
    print("=" * 55)
    print("Nota: O modelo reflete a alta eficiência e consistência do quinteto titular.")

