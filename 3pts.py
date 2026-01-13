import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predicao_especialista_3pts():
    print("Analisando métricas de arremessadores de elite...")
    
    # 1. Coletar dados da temporada atual
    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        measure_type_detailed_advanced='Base'
    ).get_data_frames()[0]

    