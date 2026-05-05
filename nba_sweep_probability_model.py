import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats

def predict_sweep_candidate():
    # Coleta estatísticas avançadas das equipes na temporada 2025-26
    # O Net Rating é a melhor métrica para medir dominância (OffRating - DefRating)
    stats = leaguedashteamstats.LeagueDashTeamStats(
        season='2025-26',
        measure_type_detailed_defense='Advanced'
    ).get_data_frames()[0]
    
    