import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predicao_melhor_por_time():
    # 1. Buscar estatísticas de todos os jogadores da temporada atual
    print("Analisando impacto de todos os jogadores da liga...")
    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26', # Ajustado para o ano atual
        measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    