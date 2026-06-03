import numpy as np
import pandas as pd

def simulate_heat_season(num_simulations=10000):
    # Calendário padrão da temporada regular da NBA
    games_in_season = 82
    
    # --- Parâmetros de Desempenho (Miami Heat) ---
    # Miami dita um ritmo físico e amarra o ataque adversário, 
    # o que mantém as médias de pontos dos dois lados mais baixas.
    heat_pts_avg = 113.8
    heat_opp_pts_avg = 110.5
    
    # Desvio padrão calibrado em 11.2 para refletir um time muito disciplinado,
    # que raramente sofre goleadas, mantendo os jogos parelhos e competitivos.
    heat_sd = 11.2
    opp_sd = 11.5
    
    sim_results = []
    
    print("Processando dados e simulando cenários para o Miami Heat...")
    
    for _ in range(num_simulations):
        # Geração de pontuações via distribuição normal para os 82 jogos
        heat_scores = np.random.normal(heat_pts_avg, heat_sd, games_in_season)
        opp_scores = np.random.normal(heat_opp_pts_avg, opp_sd, games_in_season)
        
        # Computa vitória quando o ataque de Miami supera a defesa adversária
        wins = np.sum(heat_scores > opp_scores)
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
    prob_playin_safety = (sim_series >= 44).mean() * 100   # Evitar o Play-In (Top 6 garantido)
    prob_mando_quadra = (sim_series >= 48).mean() * 100     # Mando de quadra nos Playoffs
    
    print("\n" + "=" * 55)
    print("  PREDIÇÃO DE TEMPORADA REGULAR - MIAMI HEAT 2026/27  ")
    print("=" * 55)
    print(f"Média de Vitórias Projetada: {mean_wins:.1f} - {games_in_season - mean_wins:.1f}")
    print(f"Mediana de Vitórias:          {median_wins:.0f}")
    print(f"Moda mais frequente:         {mode_wins:.0f}")
    print(f"Intervalo de Confiança (95%): {ci_lower:.0f} a {ci_upper:.0f} vitórias")
    print("-" * 55)
    print(f"Probabilidade de Vaga Direta Top 6 (44+ vitórias): {prob_playin_safety:.2f}%")
    print(f"Probabilidade de Mando de Quadra (48+ vitórias):   {prob_mando_quadra:.2f}%")
    print("=" * 55)
    print("Nota: O modelo assume a manutenção da identidade de forte ajuste defensivo.")
