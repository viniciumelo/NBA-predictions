import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats
from nba_api.stats.static import teams

def get_offensive_metrics():
    # Puxa estatísticas avançadas de todas as equipes
    stats = leaguedashteamstats.LeagueDashTeamStats(
        measure_type_detailed_defense='Advanced',
        per_mode_detailed='PerGame'
    ).get_data_frames()[0]
    
    # Colunas: Nome, Rating Ofensivo, True Shooting %, Assist Ratio e % de Turnovers
    cols = ['TEAM_NAME', 'OFF_RATING', 'TS_PCT', 'AST_PCT', 'TM_TOV_PCT']
    return stats[cols]

def predict_offensive_superiority(team_a_name, team_b_name):
    df = get_offensive_metrics()
    
    team_a = df[df['TEAM_NAME'].str.contains(team_a_name, case=False)]
    team_b = df[df['TEAM_NAME'].str.contains(team_b_name, case=False)]
    
    