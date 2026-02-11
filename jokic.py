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

    # 2. O Processo de Poda (Pruning)
    # Na LTH, removemos os parâmetros (jogos) de baixa magnitude.
    # Podamos jogos com menos de 28 minutos (Blowouts) e jogos com USG% muito baixo,
    # pois não representam a "inicialização" ideal de Jokic como pontuador.
    threshold_min = 28
    df_podado = df[df['MIN'] >= threshold_min].copy()

    