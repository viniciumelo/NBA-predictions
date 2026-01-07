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

    # 2. Função interna para prever próxima tendência usando Regressão
    def prever_categoria(serie_temporal):
        X = np.array(range(len(serie_temporal))).reshape(-1, 1)
        y = serie_temporal.values
        modelo = LinearRegression().fit(X, y)
        # Prever o próximo valor (t+1)
        proximo_indice = np.array([[len(serie_temporal)]])
        return max(0, modelo.predict(proximo_indice)[0])

    # Analisando os últimos 10 jogos para captar o "momento"
    ultimos_10 = df.tail(10)
    
    pred_1pt = prever_categoria(ultimos_10['PTS_1PT'])
    pred_2pt = prever_categoria(ultimos_10['PTS_2PT'])
    pred_3pt = prever_categoria(ultimos_10['PTS_3PT'])
    
    total_previsto = pred_1pt + pred_2pt + pred_3pt

    print(f"--- Projeção Detalhada: {nome_jogador} ---")
    print(f"Lances Livres (1pt): {pred_1pt:.1f}")
    print(f"Cestas de Campo (2pts): {pred_2pt:.1f}")
    print(f"Arremessos de Fora (3pts): {pred_3pt:.1f}")
    print(f"---------------------------------------")
    print(f"Previsão Total: {total_previsto:.1f} pontos")
