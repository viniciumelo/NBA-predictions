import pandas as pd

def predicao_lebron_winning_ticket():
    # 1. Dados da Rede Densa (Status em Fevereiro de 2026)
    # LeBron está em sua 23ª temporada, com média de ~21.8 PPG.
    stats_2026 = {
        'idade': 41,
        'MPG': 33.3,
        'PTS_AVG': 21.8,
        'AST_AVG': 6.9,
        'REB_AVG': 5.7,
        'RECENTE': [25, 22, 11, 20, 22, 28], # Últimos jogos
        'TS_PCT': 56.8  # Eficiência ainda de elite
    }

    # 2. O Processo de Poda (Pruning)
    # Na LTH, removemos os jogos onde LeBron "economiza energia" (load management em quadra).
    # Podamos o jogo de 11 pts contra Cleveland (sua ex-equipe, onde focou em passes).
    # O Winning Ticket se manifesta quando ele precisa assumir o volume (Triple-Double recente).
    sub_rede_agressiva = [p for p in stats_2026['RECENTE'] if p > 15]

   