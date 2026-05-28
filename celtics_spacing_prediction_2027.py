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
        
    # Análise descritiva da distribuição gerada
    sim_series = pd.Series(sim_results)
    mean_wins = sim_series.mean()
    median_wins = sim_series.median()
    mode_wins = sim_series.mode()[0]
    
    # Intervalo de confiança bicaudal de 95%
    ci_lower = sim_series.quantile(0.025)
    ci_upper = sim_series.quantile(0.975)
    
    # Probabilidade de atingir marcas históricas na Conferência Leste
    prob_55_plus = (sim_series >= 55).mean() * 100
    prob_60_plus = (sim_series >= 60).mean() * 100
    
    print("\n" + "=" * 55)
    print("  PREDIÇÃO DE TEMPORADA REGULAR - BOSTON CELTICS 2026/27  ")
    print("=" * 55)
    print(f"Média de Vitórias Projetada: {mean_wins:.1f} - {games_in_season - mean_wins:.1f}")
    print(f"Mediana de Vitórias:          {median_wins:.0f}")
    print(f"Moda mais frequente:         {mode_wins:.0f}")
    print(f"Intervalo de Confiança (95%): {ci_lower:.0f} a {ci_upper:.0f} vitórias")
    print("-" * 55)
    print(f"Probabilidade de vencer 55+ jogos (Top Contender):  {prob_55_plus:.2f}%")
    print(f"Probabilidade de vencer 60+ jogos (Domínio Total): {prob_60_plus:.2f}%")
    print("=" * 55)
    print("Nota: O modelo assume a manutenção da alta eficiência do perímetro.")

