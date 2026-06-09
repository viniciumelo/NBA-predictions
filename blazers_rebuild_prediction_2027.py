import numpy as np
import pandas as pd

def simulate_blazers_season(num_simulations=10000):
    # Calendário padrão da temporada regular da NBA
    games_in_season = 82
    
    # --- Parâmetros de Desempenho (Portland Trail Blazers) ---
    # Como uma equipe jovem em desenvolvimento, as médias projetadas refletem
    # um ataque veloz e talentoso, mas que ainda cede pontos devido a ajustes defensivos.
    blazers_pts_avg = 111.4
    blazers_opp_pts_avg = 117.8
    
    # Desvio padrão calibrado em 12.4 para representar a alta volatilidade.
    # Times jovens podem surpreender candidatos ao título em noites inspiradas,
    # mas também oscilar bastante em sequências de jogos fora de casa (road trips).
    blazers_sd = 12.4
    opp_sd = 11.9
    
   sim_results = []
    
    print("Processando dados e simulando cenários para o Portland Trail Blazers...")
    
    for _ in range(num_simulations):
        # Geração de pontuações via distribuição normal para os 82 jogos
        blazers_scores = np.random.normal(blazers_pts_avg, blazers_sd, games_in_season)
        opp_scores = np.random.normal(blazers_opp_pts_avg, opp_sd, games_in_season)
        
        # Computa vitória quando o ataque de Portland supera a defesa adversária
        wins = np.sum(blazers_scores > opp_scores)
        sim_results.append(wins)
        
    # Análise descritiva da distribuição gerada
    sim_series = pd.Series(sim_results)
    mean_wins = sim_series.mean()
    median_wins = sim_series.median()
    mode_wins = sim_series.mode()[0]
    
    # Intervalo de confiança bicaudal de 95%
    ci_lower = sim_series.quantile(0.025)
    ci_upper = sim_series.quantile(0.975)
    
    # Probabilidade de atingir metas de crescimento e briga por vagas no Oeste
    prob_evolution_goal = (sim_series >= 30).mean() * 100   # Bater a marca de 30 vitórias (evolução sólida)
    prob_playin_fringe = (sim_series >= 38).mean() * 100    # Briga na linha de corte do Play-In
    
    print("\n" + "=" * 55)
    print("  PREDIÇÃO DE TEMPORADA REGULAR - PORTLAND BLAZERS 2026/27  ")
    print("=" * 55)
    print(f"Média de Vitórias Projetada: {mean_wins:.1f} - {games_in_season - mean_wins:.1f}")
    print(f"Mediana de Vitórias:          {median_wins:.0f}")
    print(f"Moda mais frequente:         {mode_wins:.0f}")
    print(f"Intervalo de Confiança (95%): {ci_lower:.0f} a {ci_upper:.0f} vitórias")
    print("-" * 55)
    print(f"Probabilidade de atingir 30+ vitórias (Salto de Crescimento): {prob_evolution_goal:.2f}%")
    print(f"Probabilidade de surpreender rumo ao Play-In (38+ vitórias):   {prob_playin_fringe:.2f}%")
    print("=" * 55)
    print("Nota: O modelo incorpora a curva de aprendizado e oscilação de atletas jovens.")

