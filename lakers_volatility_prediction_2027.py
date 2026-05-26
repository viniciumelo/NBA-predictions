import numpy as np
import pandas as pd

def simulate_lakers_season(num_simulations=10000):
    # Calendário regulamentar da NBA
    games_in_season = 82
    
    # --- Parâmetros de Desempenho (LA Lakers) ---
    # Os Lakers mantêm um ataque forte focado na infiltração e garrafão,
    # mas operam com um saldo de pontos mais equilibrado na temporada regular.
    lakers_pts_avg = 116.4
    lakers_opp_pts_avg = 113.8
    
    # Desvio padrão elevado para 12.8.
    # Reflete a volatilidade de jogos onde estrelas podem ser poupadas (back-to-backs)
    # ou oscilações na rotação de suporte do perímetro.
    lakers_sd = 12.8
    opp_sd = 12.2
    
    sim_results = []
    
    print("Executando análises estatísticas para o Los Angeles Lakers...")
    
    for _ in range(num_simulations):
        # Geração de pontuações via distribuição normal para os 82 jogos
        lakers_scores = np.random.normal(lakers_pts_avg, lakers_sd, games_in_season)
        opp_scores = np.random.normal(lakers_opp_pts_avg, opp_sd, games_in_season)
        
        # Computa vitória quando o ataque do Lakers supera a defesa adversária
        wins = np.sum(lakers_scores > opp_scores)
        sim_results.append(wins)
        
    # Análise descritiva dos dados gerados
    sim_series = pd.Series(sim_results)
    mean_wins = sim_series.mean()
    median_wins = sim_series.median()
    mode_wins = sim_series.mode()[0]
    
    # Intervalo de confiança bicaudal de 95%
    ci_lower = sim_series.quantile(0.025)
    ci_upper = sim_series.quantile(0.975)
    
    # Probabilidade de garantir vaga direta ou passar pelo Play-In no Oeste
    prob_playin = (sim_series >= 41).mean() * 100         # Campanha estável de .500
    prob_playoffs_direct = (sim_series >= 47).mean() * 100 # Vaga direta no Top 6 do Oeste
    
    print("\n" + "=" * 55)
    print("  PREDIÇÃO DE TEMPORADA REGULAR - LA LAKERS 2026/27  ")
    print("=" * 55)
    print(f"Média de Vitórias Projetada: {mean_wins:.1f} - {games_in_season - mean_wins:.1f}")
    print(f"Mediana de Vitórias:          {median_wins:.0f}")
    print(f"Moda mais frequente:         {mode_wins:.0f}")
    print(f"Intervalo de Confiança (95%): {ci_lower:.0f} a {ci_upper:.0f} vitórias")
    print("-" * 55)
    print(f"Probabilidade de campanha .500+ (Play-In/Playoffs): {prob_playin:.2f}%")
    print(f"Probabilidade de Vaga Direta Top 6 (47+ vitórias):  {prob_playoffs_direct:.2f}%")
    print("=" * 55)
    print("Nota: O modelo incorpora a volatilidade por fatores de desgaste físico.")
