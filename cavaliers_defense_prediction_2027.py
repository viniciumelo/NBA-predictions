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
        
    # Análise descritiva da distribuição gerada
    sim_series = pd.Series(sim_results)
    mean_wins = sim_series.mean()
    median_wins = sim_series.median()
    mode_wins = sim_series.mode()[0]
    
    # Intervalo de confiança bicaudal de 95%
    ci_lower = sim_series.quantile(0.025)
    ci_upper = sim_series.quantile(0.975)
    
    # Probabilidade de atingir metas competitivas na Conferência Leste
    prob_50_plus = (sim_series >= 50).mean() * 100
    prob_55_plus = (sim_series >= 55).mean() * 100
    
    print("\n" + "=" * 55)
    print("  PREDIÇÃO DE TEMPORADA REGULAR - CLE CAVALIERS 2026/27  ")
    print("=" * 55)
    print(f"Média de Vitórias Projetada: {mean_wins:.1f} - {games_in_season - mean_wins:.1f}")
    print(f"Mediana de Vitórias:          {median_wins:.0f}")
    print(f"Moda mais frequente:         {mode_wins:.0f}")
    print(f"Intervalo de Confiança (95%): {ci_lower:.0f} a {ci_upper:.0f} vitórias")
    print("-" * 55)
    print(f"Probabilidade de vencer 50+ jogos (Mando de Quadra): {prob_50_plus:.2f}%")
    print(f"Probabilidade de vencer 55+ jogos (Elite do Leste):  {prob_55_plus:.2f}%")
    print("=" * 55)
    print("Nota: O modelo assume a manutenção do forte controle de garrafão.")

