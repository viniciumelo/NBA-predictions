import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predicao_faltas_allstar():
    print("Analisando perfil disciplinar para o All-Star Game...")
    
    # 1. Coletar dados da temporada (ano atual 2026)
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        measure_type_detailed_advanced='Base'
    ).get_data_frames()[0]

   