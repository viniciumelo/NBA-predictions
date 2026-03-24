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
    
    eff = (row['PTS'] + row['REB'] + row['AST'] + row['STL'] + row['BLK'] 
           - missed_fg - missed_ft - row['TOV'])
    return eff

def predict_player_performance(team_name, last_n_games=10):
    team_id = get_team_id(team_name)
    
    # Obtém a lista de jogadores ativos no elenco
    roster = commonteamroster.CommonTeamRoster(team_id=team_id).get_data_frames()[0]
    player_list = roster[['PLAYER', 'PLAYER_ID', 'NUM']]
    
    performance_report = []

    print(f"Analisando rendimento recente (últimos {last_n_games} jogos) para {team_name}...")

    