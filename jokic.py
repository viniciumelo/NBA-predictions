import pandas as pd
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog

def predicao_jokic_winning_ticket():
    print("Iniciando Poda Iterativa para isolar o 'Winning Ticket' de Nikola Jokic...")

    # 1. Coleta da Rede Densa (Histórico de 2025-26)
    player_dict = players.find_players_by_full_name("Nikola Jokic")
    player_id = player_dict[0]['id']
    
    log = playergamelog.PlayerGameLog(player_id=player_id, season='2025-26')
    df = log.get_data_frames()[0]

    