import pandas as pd
import numpy as np
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog

def analise_lottery_ticket_pontos(nome_jogador):
    # 1. Obtenção da "Rede Densa" (Dados Brutos)
    player_dict = players.find_players_by_full_name(nome_jogador)
    if not player_dict: return "Jogador não encontrado."
    player_id = player_dict[0]['id']
    
    # Coletando dados da temporada 2025-26
    log = playergamelog.PlayerGameLog(player_id=player_id, season='2025-26')
    df = log.get_data_frames()[0]
    if df.empty: return "Sem dados para a temporada."

  