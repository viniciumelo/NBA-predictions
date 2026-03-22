import pandas as pd
import numpy as np
from nba_api.stats.endpoints import leaguegamefinder, playbyplayv2
from nba_api.stats.static import teams

def get_team_id(team_abbreviation):
    nba_teams = teams.get_teams()
    return [t for t in nba_teams if t['abbreviation'] == team_abbreviation][0]['id']

