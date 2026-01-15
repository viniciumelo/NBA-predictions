import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predicao_risco_faltas():
    print("Analisando agressividade defensiva e risco de faltas...")
    
    # 1. Coletar estatísticas da temporada atual
    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        measure_type_detailed_advanced='Base'
    ).get_data_frames()[0]

   