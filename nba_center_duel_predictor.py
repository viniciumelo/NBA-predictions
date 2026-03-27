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
