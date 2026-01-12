import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predicao_melhor_por_time():
    # 1. Buscar estatísticas de todos os jogadores da temporada atual
    print("Analisando impacto de todos os jogadores da liga...")
    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26', # Ajustado para o ano atual
        measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    # 2. Limpeza e Filtro
    # Consideramos apenas jogadores que jogam pelo menos 20 minutos para evitar anomalias
    stats_filtradas = player_stats[player_stats['MIN'] >= 20].copy()

   