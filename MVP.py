import pandas as pd
from nba_api.stats.endpoints import leaguedashtreampops, leaguedashplayerstats

def predicao_mvp():
    # 1. Buscar estatísticas avançadas de todos os jogadores
    print("Coletando dados da temporada...")
    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2023-24', 
        measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    