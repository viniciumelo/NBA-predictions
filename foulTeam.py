import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats

def predicao_faltas_equipe():
    print("Analisando agressividade coletiva e métricas de arbitragem...")
    
    # 1. Coletar estatísticas das equipes na temporada atual
    # Usamos MeasureType='Base' para pegar PF (Personal Fouls)
    team_stats = leaguedashteamstats.LeagueDashTeamStats(
        season='2025-26',
        measure_type_detailed_advanced='Base'
    ).get_data_frames()[0]

    