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

    # 3. Identificação do Winning Ticket (Convergência de Pontos)
    # Calculamos a média da sub-rede estável vs. a magnitude recente (últimos 5 jogos)
    # O "Bilhete Premiado" é a média ponderada que ignora as variações irrelevantes.
    media_estavel = df_podado['PTS'].mean()
    tendencia_recente = df['PTS'].head(5).mean() 
    
    # Peso de 70% na arquitetura estável (Winning Ticket) e 30% no momento atual
    predicao_final = (media_estavel * 0.7) + (tendencia_recente * 0.3)

    print(f"\n--- RESULTADOS DA PODA (LTH) ---")
    print(f"Total de jogos analisados: {len(df)}")
    print(f"Jogos no 'Winning Ticket' (Sub-rede): {len(df_podado)}")
    print(f"Média Geral Atual: {df['PTS'].mean():.1f} pts")
    print(f"--------------------------------")
    print(f"PREDIÇÃO DE CONVERGÊNCIA: {predicao_final:.1f} PPG")
    
    return predicao_final