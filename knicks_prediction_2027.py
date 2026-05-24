import numpy as np
import pandas as pd

def simulate_knicks_season(num_simulations=10000):
    # Número de jogos na temporada regular da NBA
    games_in_season = 82
    
    # Parâmetros de desempenho baseados na identidade competitiva dos Knicks
    # Média de pontos feitos e sofridos estimada a partir do ritmo controlado (Pace)
    knicks_pts_avg = 115.5
    knicks_opp_pts_avg = 109.2
    
    # Desvio padrão para simular a volatilidade de jogos da NBA (lesões, back-to-backs, etc.)
    # Knicks costumam ser um time resiliente e de menor oscilação devido ao sistema rígido
    knicks_sd = 10.8
    opp_sd = 11.2
    
    sim_results = []
    
    print("Iniciando Simulação de Monte Carlo para os Knicks...")
    
    for _ in range(num_simulations):
        # Simulação estatística baseada em distribuição normal para os 82 jogos
        knicks_scores = np.random.normal(knicks_pts_avg, knicks_sd, games_in_season)
        opp_scores = np.random.normal(knicks_opp_pts_avg, opp_sd, games_in_season)
        
        # Vitória se os Knicks pontuarem mais que o adversário
        wins = np.sum(knicks_scores > opp_scores)
        sim_results.append(wins)
        
    # Análise de dados dos resultados gerados
    sim_series = pd.Series(sim_results)
    mean_wins = sim_series.mean()
    median_wins = sim_series.median()
    mode_wins = sim_series.mode()[0]
    
    # Intervalo de confiança de 95% (removendo os 2.5% extremos de cada lado)
    ci_lower = sim_series.quantile(0.025)
    ci_upper = sim_series.quantile(0.975)
    
    # Probabilidades de atingir metas de elite na Conferência Leste
    prob_50_plus = (sim_series >= 50).mean() * 100
    prob_55_plus = (sim_series >= 55).mean() * 100
    
    print("\n" + "=" * 55)
    print("  PREDIÇÃO DE TEMPORADA REGULAR - NY KNICKS 2026/27  ")
    print("=" * 55)
    print(f"Média de Vitórias Projetada: {mean_wins:.1f} - {games_in_season - mean_wins:.1f}")
    print(f"Mediana de Vitórias:          {median_wins:.0f}")
    print(f"Moda mais frequente:         {mode_wins:.0f}")
    print(f"Intervalo de Confiança (95%): {ci_lower:.0f} a {ci_upper:.0f} vitórias")
    print("-" * 55)
    print(f"Probabilidade de vencer 50+ jogos (Mando de Quadra): {prob_50_plus:.2f}%")
    print(f"Probabilidade de vencer 55+ jogos (Contender Top 2): {prob_55_plus:.2f}%")
    print("=" * 55)
    print("Nota: O modelo assume a manutenção do sistema defensivo de elite.")

if __name__ == "__main__":
    # Define o seed para que os resultados sejam consistentes em cada execução
    np.random.seed(44)
    simulate_knicks_season()