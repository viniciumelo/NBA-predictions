import pandas as pd

def predicao_durant_winning_ticket():
    # 1. Dados da Rede Densa (Status em Fevereiro de 2026 - Houston Rockets)
    # KD atua como o mentor ofensivo em uma rede jovem e veloz.
    stats_2026 = {
        'idade': 37,
        'MPG': 34.2,
        'PTS_AVG': 25.9,
        'FG_PCT': 52.4,
        '3P_PCT': 41.8,
        'RECENTE': [28, 31, 14, 27, 24, 33], # 14 pts foi um jogo de carga reduzida
        'FT_PCT': 91.5 # Estabilidade total na linha de lance livre
    }

    