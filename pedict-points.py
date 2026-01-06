import pandas as pd
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog

def prever_pontos_jogador(nome_jogador):
    # 1. Buscar o ID do jogador
    nba_players = players.find_players_by_full_name(nome_jogador)
    if not nba_players:
        return "Jogador não encontrado."
    
    player_id = nba_players[0]['id']

    # 2. Buscar histórico de jogos (Temporada 2023-24 ou atual)
    # Você pode alterar 'season' conforme a temporada vigente
    gamelog = playergamelog.PlayerGameLog(player_id=player_id, season='2023-24')
    df = gamelog.get_data_frames()[0]

    if df.empty:
        return "Sem dados disponíveis para este jogador na temporada."

    # Inverter o dataframe para que os jogos fiquem em ordem cronológica
    df = df.iloc[::-1].reset_index(drop=True)

    # 3. Engenharia de Dados: Criar média móvel dos últimos 5 jogos
    df['MEDIA_MOVEL_5'] = df['PTS'].rolling(window=5).mean()
    
   