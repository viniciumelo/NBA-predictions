import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats, leaguedashgs_v2
import numpy as np

# ==============================================================================
# CONFIGURAÇÃO DO DUELO
# Digite o nome exato dos dois pivôs que deseja comparar
# ==============================================================================
CENTER_A = "Nikola Jokic"
CENTER_B = "Joel Embiid"
# ==============================================================================

print(f"Analisando duelo de pivôs: {CENTER_A} vs {CENTER_B}...\n")

# 1. Obter Estatísticas Gerais de Arremesso (Temporada Atual)
# Usado para prever "Mais Cestas Seguidas"
print("Buscando dados de eficiência...")
stats = leaguedashplayerstats.LeagueDashPlayerStats(season='2023-24')
df_general = stats.get_data_frames()[0]

# 2. Obter Estatísticas de Jump Ball (Bola ao Alto)
# Usado para prever "Marca Primeiro"
print("Buscando dados de Jump Ball inicial...")
# O endpoint leaguedashgs_v2 contém dados de situações específicas
jump_stats = leaguedashgs_v2.LeagueDashGs_V2(season='2023-24', clutch_time_nullable='Last 5 Minutes')
df_jump = jump_stats.get_data_frames()[0]

