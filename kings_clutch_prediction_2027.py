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
    
    