import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerclutch
from sklearn.ensemble import GradientBoostingRegressor

# 1. Obter dados de "Clutch Time" (Momentos Decisivos)
print("Buscando dados de performance em momentos decisivos (Clutch)...")
clutch_stats = leaguedashplayerclutch.LeagueDashPlayerClutch(
    season='2023-24', 
    clutch_time_nullable='Last 5 Minutes', 
    point_diff_nullable='5'
)
df_clutch = clutch_stats.get_data_frames()[0]

