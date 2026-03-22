import pandas as pd
import numpy as np
from nba_api.stats.endpoints import leaguegamefinder, playbyplayv2
from nba_api.stats.static import teams

def get_team_id(team_abbreviation):
    nba_teams = teams.get_teams()
    return [t for t in nba_teams if t['abbreviation'] == team_abbreviation][0]['id']

def analyze_scoring_tendencies(team_id, num_games=20):
    # Busca os últimos jogos da equipe
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team_id)
    games = gamefinder.get_data_frames()[0]
    recent_games = games.head(num_games)
    
    first_point_count = 0
    last_point_count = 0
    
    