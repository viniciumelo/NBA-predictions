import pandas as pd
from nba_api.stats.endpoints import leaguegamefinder, playergameastypebygame
from nba_api.stats.static import teams
from sklearn.ensemble import RandomForestRegressor
import numpy as np

# 1. Configurações Iniciais
TEAM_NAME = 'Los Angeles Lakers' # Altere para o time desejado
team_info = [t for t in teams.get_teams() if t['full_name'] == TEAM_NAME][0]
team_id = team_info['id']

# 2. Buscar jogos recentes do time para coletar dados de treino
gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team_id)
games = gamefinder.get_data_frames()[0]
recent_games_ids = games.head(10)['GAME_ID'].tolist() # Últimos 10 jogos

