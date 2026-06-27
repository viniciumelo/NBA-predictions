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
    
    