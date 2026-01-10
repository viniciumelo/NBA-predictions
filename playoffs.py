import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats

def predicao_playoffs(time_a, time_b):
    # 1. Coletar estatísticas de equipes focadas em 'Playoffs'
    # O parâmetro MeasureType='Advanced' traz o NetRating (métrica de ouro)
    stats = leaguedashteamstats.LeagueDashTeamStats(
        season='2023-24', 
        season_type_all_star='Playoffs',
        measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    def get_team_metrics(team_name):
        team_data = stats[stats['TEAM_NAME'] == team_name]
        if team_data.empty: return None
        return {
            'net_rating': team_data['NET_RATING'].values[0],
            'off_rating': team_data['OFF_RATING'].values[0],
            'def_rating': team_data['DEF_RATING'].values[0],
            'true_shooting': team_data['TS_PCT'].values[0]
        }

    