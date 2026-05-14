import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats

def predict_nba_finalists():
    # Coleta de dados avançados da temporada 2025-26
    print("Analisando métricas de elite para as Finais...")
    team_stats = leaguedashteamstats.LeagueDashTeamStats(
        season='2025-26',
        measure_type_detailed_defense='Advanced'
    ).get_data_frames()[0]
