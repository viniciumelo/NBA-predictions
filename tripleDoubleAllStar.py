import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predicao_triple_double_allstar():
    print("Analisando versatilidade para Triple-Double no All-Star...")
    
    # 1. Coletar dados da temporada atual (para ver quem está produzindo em várias áreas)
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        measure_type_detailed_advanced='Base'
    ).get_data_frames()[0]

    