import numpy as np
import pandas as pd

def simulate_spurs_season(num_simulations=10000):
    # Calendário padrão da temporada regular da NBA
    games_in_season = 82
    
    # --- Parâmetros de Projeção (Fator de Evolução) ---
    # Modelamos um incremento na média de pontos feitos e uma redução nos pontos sofridos,
    # refletindo o impacto defensivo gerado pelo amadurecimento do Wemby na área pintada.
    spurs_pts_avg = 114.8
    spurs_opp_pts_avg = 111.2
    
    # Desvio padrão ligeiramente maior (12.2) para representar a volatilidade natural 
    # de elencos jovens (picos de grande desempenho misturados com oscilações de experiência)
    spurs_sd = 12.2
    opp_sd = 11.8
    
    sim_results = []
    
    print("Executando simulações para a temporada do San Antonio Spurs...")
    
    for _ in range(num_simulations):
        # Geração de pontuações baseada em distribuição normal para os 82 confrontos
        spurs_scores = np.random.normal(spurs_pts_avg, spurs_sd, games_in_season)
        opp_scores = np.random.normal(spurs_opp_pts_avg, opp_sd, games_in_season)
        
        # Computa vitória quando o ataque supera a defesa adversária
        wins = np.sum(spurs_scores > opp_scores)
        sim_results.append(wins)
        
    # Agrupamento e análise dos dados simulados
    sim_series = pd.Series(sim_results)
    mean_wins = sim_series.mean()
    median_wins = sim_series.median()
    mode_wins = sim_series.mode()[0]
    
    # Intervalo de confiança bicaudal de 95%
    ci_lower = sim_series.quantile(0.025)
    ci_upper = sim_series.quantile(0.975)
    
    # Probabilidade de atingir marcos competitivos importantes na Conferência Oeste
    prob_playin = (sim_series >= 41).mean() * 100  # Aproveitamento de .500 (Briga por Play-In/Playoffs)
    prob_playoffs_direct = (sim_series >= 46).mean() * 100 # Vaga direta no Top 6
    
    print("\n" + "=" * 55)
    print("  PREDIÇÃO DE TEMPORADA REGULAR - SA SPURS 2026/27  ")
    print("=" * 55)
    print(f"Média de Vitórias Projetada: {mean_wins:.1f} - {games_in_season - mean_wins:.1f}")
    print(f"Mediana de Vitórias:          {median_wins:.0f}")
    print(f"Moda mais frequente:         {mode_wins:.0f}")
    print(f"Intervalo de Confiança (95%): {ci_lower:.0f} a {ci_upper:.0f} vitórias")
    print("-" * 55)
    print(f"Probabilidade de campanha .500+ (Play-In/Playoffs): {prob_playin:.2f}%")
    print(f"Probabilidade de Top 6 Direto (46+ vitórias):       {prob_playoffs_direct:.2f}%")
    print("=" * 55)
    print("Nota: O modelo incorpora o salto de eficiência defensiva esperado.")

if __name__ == "__main__":
    # Semente fixa para reprodutibilidade dos dados estatísticos
    np.random.seed(21)
    simulate_spurs_season()