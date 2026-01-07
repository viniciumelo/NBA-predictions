import pandas as pd
import numpy as np
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
from sklearn.linear_model import LinearRegression

def analise_detalhada_pontos(nome_jogador):
    # 1. Obter dados
    player_dict = players.find_players_by_full_name(nome_jogador)
    player_id = player_dict[0]['id']
    
    # Pegando dados da temporada atual
    log = playergamelog.PlayerGameLog(player_id=player_id, season='2023-24')
    df = log.get_data_frames()[0]
    
    # Inverter para ordem cronológica e selecionar colunas chave
    df = df.iloc[::-1].reset_index()
    
    # Preparando as categorias de pontos
    # FTM = Free Throws Made (1pt)
    # FG2M = FGM (Total) - FG3M (3pts)
    df['PTS_1PT'] = df['FTM']
    df['PTS_2PT'] = (df['FGM'] - df['FG3M']) * 2
    df['PTS_3PT'] = df['FG3M'] * 3

    