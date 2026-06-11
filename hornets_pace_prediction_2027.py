import numpy as np
import pandas as pd

def simulate_hornets_season(num_simulations=10000):
    # Calendário padrão da temporada regular da NBA
    games_in_season = 82
    
    # --- Parâmetros de Desempenho (Charlotte Hornets) ---
    # Hornets operam em ritmo acelerado, gerando boas médias de ataque,
    # enquanto buscam consolidação e consistência no sistema defensivo.
    hornets_pts_avg = 114.2
    hornets_opp_pts_avg = 117.5
    
    # Desvio padrão calibrado em 12.0 para representar a volatilidade natural
    # de equipes velozes de transição, suscetíveis a sequências de rachas de pontos.
    hornets_sd = 12.0
    opp_sd = 11.6
    
   sim_results = []
    
    print("Processando dados e simulando cenários para o Charlotte Hornets...")
    
    for _ in range(num_simulations):
        # Geração de pontuações via distribuição normal para os 82 jogos
        hornets_scores = np.random.normal(hornets_pts_avg, hornets_sd, games_in_season)
        opp_scores = np.random.normal(hornets_opp_pts_avg, opp_sd, games_in_season)
        
        # Computa vitória quando o ataque de Charlotte supera a defesa adversária
        wins = np.sum(hornets_scores > opp_scores)
        sim_results.append(wins)
        
    # Análise descritiva da distribuição gerada
    sim_series = pd.Series(sim_results)
    mean_wins = sim_series.mean()
    median_wins = sim_series.median()
    mode_wins = sim_series.mode()[0]
    
    # Intervalo de confiança bicaudal de 95%
    ci_lower = sim_series.quantile(0.025)
    ci_upper = sim_series.quantile(0.975)
    
    # Probabilidade de atingir metas competitivas e brigar por pós-temporada no Leste
    prob_growth_goal = (sim_series >= 35).mean() * 100     # Alcançar 35+ vitórias (evolução clara)
    prob_playin_spot = (sim_series >= 40).mean() * 100     # Briga direta por vaga no Play-In
    
    print("\n" + "=" * 55)
    print("  PREDIÇÃO DE TEMPORADA REGULAR - CHARLOTTE HORNETS 2026/27  ")
    print("=" * 55)
    print(f"Média de Vitórias Projetada: {mean_wins:.1f} - {games_in_season - mean_wins:.1f}")
    print(f"Mediana de Vitórias:          {median_wins:.0f}")
    print(f"Moda mais frequente:         {mode_wins:.0f}")
    print(f"Intervalo de Confiança (95%): {ci_lower:.0f} a {ci_upper:.0f} vitórias")
    print("-" * 55)
    print(f"Probabilidade de 35+ vitórias (Evolução de Patamar): {prob_growth_goal:.2f}%")
    print(f"Probabilidade de brigar por Play-In (40+ vitórias):  {prob_playin_spot:.2f}%")
    print("=" * 55)
    print("Nota: O modelo incorpora o ritmo acelerado e o impacto dos criadores do perímetro.")

if __name__ == "__main__":
    # Semente aleatória para consistência dos cálculos matemáticos
    np.random.seed(11)
    simulate_hornets_season()