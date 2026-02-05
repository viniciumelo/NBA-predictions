import pandas as pd
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog

def encontrar_bilhete_premiado_pts(nome_jogador):
    print(f"Buscando a sub-rede vencedora para {nome_jogador}...")
    
    # 1. Identificação do Jogador
    nba_players = players.find_players_by_full_name(nome_jogador)
    if not nba_players: return "Não encontrado."
    player_id = nba_players[0]['id']

    # 2. Coleta da 'Rede Densa' (Histórico Completo da Temporada 2025-26)
    df = playergamelog.PlayerGameLog(player_id=player_id, season='2025-26').get_data_frames()[0]
    if df.empty: return "Sem dados."

    # 3. Processo de Poda (Pruning)
    # Na LTH, removemos os pesos (jogos) de baixa magnitude ou outliers.
    # Vamos 'podar' os 20% piores jogos da temporada para isolar o 'winning ticket'
    # de quando o jogador está saudável e engajado.
    threshold_poda = df['PTS'].quantile(0.20)
    sub_rede_vencedora = df[df['PTS'] > threshold_poda].copy()

    # 4. Cálculo do Bilhete Vencedor (Predição)
    # Analisamos a média da sub-rede podada vs a tendência recente (últimos 3 jogos)
    # Isso equilibra a 'arquitetura' do jogador com o 'treinamento' recente.
    potencial_base = sub_rede_vencedora['PTS'].mean()
    tendencia_recente = df['PTS'].head(3).mean() # head(3) pois o log é decrescente
    
    