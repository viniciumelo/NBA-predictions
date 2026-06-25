import numpy as np
import pandas as pd

def simulate_magic_season(num_simulations=10000):
    # Calendário regulamentar da NBA
    games_in_season = 82
    
    # --- Parâmetros de Desempenho (Orlando Magic) ---
    # Orlando dita o ritmo através de uma defesa sufocante, mantendo a média 
    # de pontos dos adversários em patamares baixos, compensando um ataque focado em meia-quadra.
    magic_pts_avg = 114.8
    magic_opp_pts_avg = 109.5
    
    # Desvio padrão calibrado em 10.7 para representar a previsibilidade da defesa.
    # Como a intensidade defensiva do Magic é consistente e viaja bem (funciona fora de casa),
    # o time sofre menos apagões estatísticos severos.
    magic_sd = 10.7
    opp_sd = 11.1

    sim_results = []
    
    print("Processando dados e calculando projeções para o Orlando Magic...")
    
    for _ in range(num_simulations):
        # Geração de pontuações via distribuição normal para os 82 jogos
        magic_scores = np.random.normal(magic_pts_avg, magic_sd, games_in_season)
        opp_scores = np.random.normal(magic_opp_pts_avg, opp_sd, games_in_season)
        
        # Computa vitória se o ataque de Orlando superar a defesa adversária
        wins = np.sum(magic_scores > opp_scores)
        sim_results.append(wins)

    # Análise descritiva da distribuição gerada
    sim_series = pd.Series(sim_results)
    mean_wins = sim_series.mean()
    median_wins = sim_series.median()
    mode_wins = sim_series.mode()[0]
    
    # Intervalo de confiança bicaudal de 95%
    ci_lower = sim_series.quantile(0.025)
    ci_upper = sim_series.quantile(0.975)
    
    # Probabilidade de atingir metas competitivas no topo da Conferência Leste
    prob_48_plus = (sim_series >= 48).mean() * 100         # Briga forte por mando de quadra (Top 4)
    prob_53_plus = (sim_series >= 53).mean() * 100         # Prateleira de elite absoluta do Leste
    
    print("\n" + "=" * 55)
    print("  PREDIÇÃO DE TEMPORADA REGULAR - ORLANDO MAGIC 2026/27  ")
    print("=" * 55)
    print(f"Média de Vitórias Projetada: {mean_wins:.1f} - {games_in_season - mean_wins:.1f}")
    print(f"Mediana de Vitórias:          {median_wins:.0f}")
    print(f"Moda mais frequente:         {mode_wins:.0f}")
    print(f"Intervalo de Confiança (95%): {ci_lower:.0f} a {ci_upper:.0f} vitórias")
    print("-" * 55)
    print(f"Probabilidade de 48+ vitórias (Mando de Quadra/Top 4): {prob_48_plus:.2f}%")
    print(f"Probabilidade de 53+ vitórias (Elite do Leste):        {prob_53_plus:.2f}%")
    print("=" * 55)
    print("Nota: O modelo reflete a sustentabilidade baseada no rating defensivo.")

if __name__ == "__main__":
    # Semente aleatória para consistência dos resultados estatísticos
    np.random.seed(48)
    simulate_magic_season()