import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats

def predict_sweep_candidate():
    # Coleta estatísticas avançadas das equipes na temporada 2025-26
    # O Net Rating é a melhor métrica para medir dominância (OffRating - DefRating)
    stats = leaguedashteamstats.LeagueDashTeamStats(
        season='2025-26',
        measure_type_detailed_defense='Advanced'
    ).get_data_frames()[0]
    
    # Selecionamos métricas que indicam potencial de "varrida"
    # 1. NET_RATING: Dominância geral
    # 2. W_PCT: Consistência de vitória
    df = stats[['TEAM_NAME', 'W_PCT', 'NET_RATING']].copy()
    