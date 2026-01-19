import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predicao_all_star_chance():
    print("Calculando probabilidades de All-Star baseadas em métricas históricas...")
    
    # 1. Coletar dados da temporada (Representando o 'Ano Anterior' ou Atual)
    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2024-25',
        measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    