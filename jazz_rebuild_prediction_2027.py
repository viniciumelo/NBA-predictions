import numpy as np
import pandas as pd

def simulate_jazz_season(num_simulations=10000):
    # Calendário padrão da temporada regular da NBA
    games_in_season = 82
    
    # --- Parâmetros de Desempenho (Utah Jazz) ---
    # O Jazz costuma manter um ataque com bom aproveitamento de arremessos de fora,
    # balanceado por ajustes e busca por consistência no sistema defensivo.
    jazz_pts_avg = 113.5
    jazz_opp_pts_avg = 118.2
    
    # Desvio padrão calibrado em 12.2 para capturar a alta volatilidade de elencos jovens.
    # O fator altitude em casa costuma gerar picos de grande desempenho ofensivo,
    # enquanto a juventude da rotação introduz variações em jogos parelhos.
    jazz_sd = 12.2
    opp_sd = 11.7
    
    sim_results = []
    
    