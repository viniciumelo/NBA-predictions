import numpy as np
import pandas as pd

def simulate_pelicans_season(num_simulations=10000):
    # Calendário padrão da temporada regular da NBA
    games_in_season = 82
    
    # --- Parâmetros de Desempenho (New Orleans Pelicans) ---
    # New Orleans apresenta um ataque eficiente punindo o garrafão adversário,
    # mantendo um saldo positivo seguro quando a rotação principal está saudável.
    pelicans_pts_avg = 116.8
    pelicans_opp_pts_avg = 113.2
    
    # Desvio padrão elevado para 12.5.
    # Reflete a volatilidade natural gerada por fatores de gerenciamento de carga,
    # desgaste físico ao longo de 82 jogos e mudanças pontuais no quinteto titular.
    pelicans_sd = 12.5
   