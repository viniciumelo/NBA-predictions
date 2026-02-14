import pandas as pd

def predicao_luka_winning_ticket():
    # 1. Dados da Rede Densa (Status em Fevereiro de 2026)
    # Luka está em uma temporada histórica, brigando pelo MVP com médias de Triple-Double.
    stats_2026 = {
        'GP': 52,
        'MPG': 37.8,
        'PTS_AVG': 34.2,
        'AST_AVG': 9.8,
        'REB_AVG': 9.2,
        'RECENTE': [38, 41, 18, 32, 45, 29], # Oscilação natural de alto volume
        'USG_PCT': 36.5, # Um dos maiores da liga
        'TS_PCT': 59.4
    }

    # 2. O Processo de Poda (Pruning)
    # Na LTH, podamos os neurônios (jogos) de baixa magnitude.
    # Removemos o jogo de 18 pts (ruído), onde ele enfrentou uma marcação tripla 
    # ou teve fadiga por jogos seguidos (back-to-back).
    sub_rede_estavel = [p for p in stats_2026['RECENTE'] if p > 25]

    