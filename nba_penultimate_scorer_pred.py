import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerclutch
from sklearn.ensemble import RandomForestRegressor

# 1. Buscar dados de Clutch (Últimos 5 min, diferença de até 5 pontos)
print("Analisando dados de momentos decisivos da NBA...")
clutch_stats = leaguedashplayerclutch.LeagueDashPlayerClutch(
    season='2023-24', 
    clutch_time_nullable='Last 5 Minutes', 
    point_diff_nullable='5'
)
df_clutch = clutch_stats.get_data_frames()[0]

# 2. Lógica para o "Penúltimo Ponto"
# O penúltimo ponto geralmente pertence a:
# A) Quem bate muitos lances livres (FTA)
# B) Quem tem alto volume de arremessos (FGA) mas não necessariamente a maior eficiência final
df_clutch['PENULTIMATE_SCORE_INDEX'] = (df_clutch['FTA'] * 0.6) + (df_clutch['FGA'] * 0.4)

