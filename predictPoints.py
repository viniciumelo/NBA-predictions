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
    
    # Pegar os dados mais recentes
    ultimos_pontos = df['PTS'].iloc[-1]
    media_temporada = df['PTS'].mean()
    predicao_proximo_jogo = df['MEDIA_MOVEL_5'].iloc[-1]

    print(f"--- Resultados para: {nome_jogador} ---")
    print(f"Média na Temporada: {media_temporada:.1f} pts")
    print(f"Pontos no Último Jogo: {ultimos_pontos}")
    print(f"Predição para o Próximo Jogo (Base 5 últimas): {predicao_proximo_jogo:.1f} pts")
    
    return predicao_proximo_jogo

# Exemplo de uso
prever_pontos_jogador("LeBron James")