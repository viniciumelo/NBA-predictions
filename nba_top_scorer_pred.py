import pandas as pd
from nba_api.stats.endpoints import leaguegamefinder, playergameastypebygame
from nba_api.stats.static import teams
from sklearn.ensemble import RandomForestRegressor
import numpy as np

# 1. Configurações Iniciais
TEAM_NAME = 'Los Angeles Lakers' # Altere para o time desejado
team_info = [t for t in teams.get_teams() if t['full_name'] == TEAM_NAME][0]
team_id = team_info['id']

