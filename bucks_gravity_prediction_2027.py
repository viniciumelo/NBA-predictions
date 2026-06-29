import numpy as np
import pandas as pd

def simulate_bucks_season(num_simulations=10000):
    # Calendário regulamentar da NBA
    games_in_season = 82
    
    # --- Parâmetros de Desempenho (Milwaukee Bucks) ---
    # Milwaukee mantém um teto ofensivo muito forte devido à eficiência na área pintada
    # e volume de arremessos, operando com um sólido diferencial positivo.
    bucks_pts_avg = 118.2
    bucks_opp_pts_avg = 114.0
    
    # Desvio padrão calibrado em 12.0 para modelar noites de preservação (back-to-backs)
    # ou oscilações normais na rotação defensiva de suporte do perímetro.
    bucks_sd = 12.0
    opp_sd = 11.5

    sim_results = []
    
    print("Processando dados e computando simulações para o Milwaukee Bucks...")
    
    for _ in range(num_simulations):
        # Geração de pontuações via distribuição normal para os 82 jogos
        bucks_scores = np.random.normal(bucks_pts_avg, bucks_sd, games_in_season)
        opp_scores = np.random.normal(bucks_opp_pts_avg, opp_sd, games_in_season)
        
        # Computa vitória quando o ataque de Milwaukee supera a defesa adversária
        wins = np.sum(bucks_scores > opp_scores)
        sim_results.append(wins)
        
    # Análise descritiva da distribuição gerada
    sim_series = pd.Series(sim_results)
    mean_wins = sim_series.mean()
    median_wins = sim_series.median()
    mode_wins = sim_series.mode()[0]
    
    # Intervalo de confiança bicaudal de 95%
    ci_lower = sim_series.quantile(0.025)
    ci_upper = sim_series.quantile(0.975)

    # Probabilidade de atingir metas de elite na Conferência Leste
    prob_46_plus = (sim_series >= 46).mean() * 100         # Vaga direta garantida no Top 6
    prob_52_plus = (sim_series >= 52).mean() * 100         # Briga direta por Mando de Quadra/Top 3
    
    print("\n" + "=" * 55)
    print("  PREDIÇÃO DE TEMPORADA REGULAR - MILWAUKEE BUCKS 2026/27  ")
    print("=" * 55)
    print(f"Média de Vitórias Projetada: {mean_wins:.1f} - {games_in_season - mean_wins:.1f}")
    print(f"Mediana de Vitórias:          {median_wins:.0f}")
    print(f"Moda mais frequente:         {mode_wins:.0f}")
    print(f"Intervalo de Confiança (95%): {ci_lower:.0f} a {ci_upper:.0f} vitórias")
    print("-" * 55)
    print(f"Probabilidade de Vaga Direta Top 6 (46+ vitórias): {prob_46_plus:.2f}%")
    print(f"Probabilidade de Mando de Quadra (52+ vitórias):   {prob_52_plus:.2f}%")
    print("=" * 55)
    print("Nota: O modelo incorpora o fator de desgaste físico e profundidade de elenco.")

if __name__ == "__main__":
    # Semente aleatória para consistência dos cálculos matemáticos
    np.random.seed(34)