import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats
from sklearn.ensemble import GradientBoostingRegressor

# 1. Obter estatísticas detalhadas da temporada atual
print("Buscando dados da NBA...")
stats = leaguedashplayerstats.LeagueDashPlayerStats(season='2023-24') # Ajuste a temporada se necessário
df = stats.get_data_frames()[0]

