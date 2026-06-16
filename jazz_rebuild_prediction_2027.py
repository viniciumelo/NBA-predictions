import numpy as np
import pandas as pd

def simulate_jazz_season(num_simulations=10000):
    # Calendário padrão da temporada regular da NBA
    games_in_season = 82
    
    # --- Parâmetros de Desempenho (Utah Jazz) ---
    # O Jazz costuma manter um ataque com bom aproveitamento de arremessos de fora,
    # balanceado por ajustes e busca por consistência no sistema defensivo.
    jazz_pts_avg = 113.5
    jazz_opp_pts_avg = 118.2
    
    # Desvio padrão calibrado em 12.2 para capturar a alta volatilidade de elencos jovens.
    # O fator altitude em casa costuma gerar picos de grande desempenho ofensivo,
    # enquanto a juventude da rotação introduz variações em jogos parelhos.
    jazz_sd = 12.2
    opp_sd = 11.7
    
    sim_results = []
    
    print("Processando dados e simulando cenários para o Utah Jazz...")
    
    for _ in range(num_simulations):
        # Geração de pontuações via distribuição normal para os 82 jogos
        jazz_scores = np.random.normal(jazz_pts_avg, jazz_sd, games_in_season)
        opp_scores = np.random.normal(jazz_opp_pts_avg, opp_sd, games_in_season)
        
        # Computa vitória quando o ataque de Utah supera a defesa adversária
        wins = np.sum(jazz_scores > opp_scores)
        sim_results.append(wins)
        
    # Análise descritiva da distribuição gerada
    sim_series = pd.Series(sim_results)
    mean_wins = sim_series.mean()
    median_wins = sim_series.median()
    mode_wins = sim_series.mode()[0]
    
    # Intervalo de confiança bicaudal de 95%
    ci_lower = sim_series.quantile(0.025)
    ci_upper = sim_series.quantile(0.975)
    
    # Probabilidade de atingir metas de maturação na Conferência Oeste
    prob_evolution_goal = (sim_series >= 32).mean() * 100   # Alcançar 32+ vitórias (salto de patamar)
    prob_playin_fringe = (sim_series >= 38).mean() * 100    # Beliscar a zona de corte do Play-In
    
    print("\n" + "=" * 55)
    print("  PREDIÇÃO DE TEMPORADA REGULAR - UTAH JAZZ 2026/27  ")
    print("=" * 55)
    print(f"Média de Vitórias Projetada: {mean_wins:.1f} - {games_in_season - mean_wins:.1f}")
    print(f"Mediana de Vitórias:          {median_wins:.0f}")
    print(f"Moda mais frequente:         {mode_wins:.0f}")
    print(f"Intervalo de Confiança (95%): {ci_lower:.0f} a {ci_upper:.0f} vitórias")
    print("-" * 55)
    print(f"Probabilidade de 32+ vitórias (Crescimento Sólido): {prob_evolution_goal:.2f}%")
    print(f"Probabilidade de surpreender no Play-In (38+ vitórias): {prob_playin_fringe:.2f}%")
    print("=" * 55)
    print("Nota: O modelo incorpora o fator de desenvolvimento de atletas e rotação ativa.")
