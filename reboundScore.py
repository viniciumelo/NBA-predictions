import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predicao_rebotes():
    print("Analisando presença de garrafão e eficiência de rebotes...")
    
    # 1. Coletar estatísticas avançadas da temporada
    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

   