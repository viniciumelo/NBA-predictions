import pandas as pd
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog

def encontrar_bilhete_premiado_pts(nome_jogador):
    print(f"Buscando a sub-rede vencedora para {nome_jogador}...")
    
    # 1. Identificação do Jogador
    nba_players = players.find_players_by_full_name(nome_jogador)
    if not nba_players: return "Não encontrado."
    player_id = nba_players[0]['id']

   