import numpy as np
import pandas as pd

def simulate_kings_season(num_simulations=10000):
    # Calendário regulamentar da NBA
    games_in_season = 82
    
    # --- Parâmetros de Desempenho (Sacramento Kings) ---
    # Sacramento mantém um ataque de alto volume e movimentação de bola fluida,
    # enquanto a defesa busca consistência física para segurar placares.
    kings_pts_avg = 117.5
    kings_opp_pts_avg = 114.2
    
    # Desvio padrão calibrado em 11.5 para representar o teto ofensivo sólido,
    # balanceado pelas flutuações comuns em jogos decididos nos minutos finais (clutch).
    kings_sd = 11.5
    opp_sd = 11.2
    
   sim_results = []
    
    print("Processando dados e simulando cenários para o Sacramento Kings...")
    
    for _ in range(num_simulations):
        # Geração de pontuações via distribuição normal para os 82 jogos
        kings_scores = np.random.normal(kings_pts_avg, kings_sd, games_in_season)
        opp_scores = np.random.normal(kings_opp_pts_avg, opp_sd, games_in_season)
        
        # Computa vitória quando o ataque de Sacramento supera a defesa adversária
        wins = np.sum(kings_scores > opp_scores)
        sim_results.append(wins)
        
    # Análise descritiva da distribuição gerada
    sim_series = pd.Series(sim_results)
    mean_wins = sim_series.mean()
   