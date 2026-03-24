import pandas as pd
from nba_api.stats.endpoints import commonteamroster, playergamelogs
from nba_api.stats.static import teams
import time

def get_team_id(team_name):
    nba_teams = teams.get_teams()
    return [t for t in nba_teams if team_name.lower() in t['full_name'].lower()][0]['id']

def calculate_efficiency(row):
    # Fórmula Padrão de Eficiência da NBA:
    # (PTS + REB + AST + STL + BLK - Missed FG - Missed FT - TOV)
    missed_fg = row['FGA'] - row['FGM']
    missed_ft = row['FTA'] - row['FTM']
    
    