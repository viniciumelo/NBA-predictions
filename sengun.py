import pandas as pd

def predicao_sengun_lottery_ticket():
    # 1. Dados da Rede Densa (Temporada 2025-26 até Fev/2026)
    # Alperen Şengün consolidou-se como All-Star com médias de elite.
    stats_2026 = {
        'GP': 45,
        'MPG': 34.0,
        'PTS_AVG': 20.8,
        'LAST_5': [22, 17, 7, 13, 39], # Oscilação recente devido a fadiga/lesão
        'USG_PCT': 26.6,
        'TS_PCT': 55.1
    }

    # 2. O Processo de Poda (Pruning)
    # Na LTH, removemos os 'pesos' que não representam a arquitetura real.
    # Podamos o jogo de 7 pts (vs Charlotte) e 13 pts (vs Boston), onde 
    # limitações físicas e blowouts criaram ruído na rede.
    jogos_validos = [p for p in stats_2026['LAST_5'] if p > 15] # Poda de jogos atípicos
    

predicao_sengun_lottery_ticket()