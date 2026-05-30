import numpy as np
import pandas as pd

def simulate_mavericks_season(num_simulations=10000):
    # Calendário padrão da temporada regular da NBA
    games_in_season = 82
    
    # --- Parâmetros de Desempenho (Dallas Mavericks) ---
    # Dallas possui um ataque de elite impulsionado por isolações e espaçamento,
    # gerando médias altas de pontuação, enquanto a defesa opera em nível competitivo estável.
    mvs_pts_avg = 118.5
    mvs_opp_pts_avg = 113.2
    
    # Desvio padrão calibrado em 11.8 para representar o teto explosivo do ataque
    # (noites com alto volume de bolas de 3) combinada com a dependência do núcleo principal.
    mvs_sd = 11.8
    opp_sd = 11.4
    
    sim_results = []
    
    print("Processando dados e simulando cenários para o Dallas Mavericks...")
    
    for _ in range(num_simulations):
        # Geração de pontuações via distribuição normal para os 82 jogos
        mvs_scores = np.random.normal(mvs_pts_avg, mvs_sd, games_in_season)
        opp_scores = np.random.normal(mvs_opp_pts_avg, opp_sd, games_in_season)
        
        # Computa vitória quando o ataque de Dallas supera a defesa adversária
        wins = np.sum(mvs_scores > opp_scores)
        sim_results.append(wins)
        
    # Análise descritiva da distribuição gerada
    sim_series = pd.Series(sim_results)
    mean_wins = sim_series.mean()
    median_wins = sim_series.median()
    mode_wins = sim_series.mode()[0]
    
    # Intervalo de confiança bicaudal de 95%
    ci_lower = sim_series.quantile(0.025)
    ci_upper = sim_series.quantile(0.975)
    
    # Probabilidade de atingir metas competitivas na acirrada Conferência Oeste
    prob_50_plus = (sim_series >= 50).mean() * 100         # Vaga sólida nos Playoffs
    prob_55_plus = (sim_series >= 55).mean() * 100         # Briga pelo Top 2 do Oeste
    
    print("\n" + "=" * 55)
    print("  PREDIÇÃO DE TEMPORADA REGULAR - DALLAS MAVS 2026/27  ")
    print("=" * 55)
    print(f"Média de Vitórias Projetada: {mean_wins:.1f} - {games_in_season - mean_wins:.1f}")
    print(f"Mediana de Vitórias:          {median_wins:.0f}")
    print(f"Moda mais frequente:         {mode_wins:.0f}")
    print(f"Intervalo de Confiança (95%): {ci_lower:.0f} a {ci_upper:.0f} vitórias")
    print("-" * 55)
    print(f"Probabilidade de vencer 50+ jogos (Vaga Direta): {prob_50_plus:.2f}%")
    print(f"Probabilidade de vencer 55+ jogos (Elite do Oeste): {prob_55_plus:.2f}%")
    print("=" * 55)
    print("Nota: O modelo assume a alta eficiência ofensiva gerada pelo espaçamento de quadra.")

if __name__ == "__main__":
    # Semente aleatória para consistência dos cálculos matemáticos
    np.random.seed(77)
    simulate_mavericks_season()