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

# 3. Coletar estatísticas de jogadores nesses jogos
all_stats = []
for gid in recent_games_ids:
    # Busca o boxscore detalhado de cada jogo
    from nba_api.stats.endpoints import boxscoretraditionalv2
    box = boxscoretraditionalv2.BoxScoreTraditionalV2(game_id=gid)
    df = box.get_data_frames()[0]
    all_stats.append(df[df['TEAM_ID'] == team_id])

train_df = pd.concat(all_stats)

# 4. Engenharia de Variáveis Simples (Features)
# Vamos prever 'PTS' com base em Minutos (convertidos), Tentativas de Arremesso e Faltas
train_df['MIN_CLEAN'] = train_df['MIN'].str.split(':').str[0].replace('', 0).astype(float)
features = ['MIN_CLEAN', 'FGA', 'FTA']
X = train_df[features].fillna(0)
y = train_df['PTS'].fillna(0)

