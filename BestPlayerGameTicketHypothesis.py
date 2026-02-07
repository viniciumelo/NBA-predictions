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

    # Engenharia de Atributos (Categorias de Pontuação)
    df['PTS_1PT'] = df['FTM']
    df['PTS_2PT'] = (df['FGM'] - df['FG3M']) * 2
    df['PTS_3PT'] = df['FG3M'] * 3

    # 2. O Processo de Poda (Pruning)
    # Na LTH, removemos os 'pesos' de baixa magnitude. 
    # Aqui, podamos os jogos onde o volume de jogo foi atípico (lesões, pouco tempo de quadra).
    # O Winning Ticket é o jogador atuando em sua 'inicialização ideal'.
    threshold_minutos = df['MIN'].quantile(0.25) # Podar os 25% dos jogos com menos minutos
    sub_rede_vencedora = df[df['MIN'] >= threshold_minutos].copy()

    # 3. Identificação da Convergência (Média do Bilhete Premiado)
    # Em vez de regressão (que pode ser enganada por um único jogo ruim), 
    # usamos a média da sub-rede podada, ajustada pelo 'momento' (últimos 5 jogos).
    
    def calcular_ticket_score(coluna):
        # Média da arquitetura estável (sub-rede)
        base_estavel = sub_rede_vencedora[coluna].mean()
       