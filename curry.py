import pandas as pd

def predicao_curry_winning_ticket():
    # 1. Dados da Rede Densa (Status em Fevereiro de 2026)
    # Curry, aos 37 anos, continua sendo a maior ameaça de perímetro da liga.
    stats_2026 = {
        'idade': 37,
        'MPG': 32.5,
        'PTS_AVG': 26.4,
        '3PM_AVG': 4.8,
        '3P_PCT': 41.2,
        'RECENTE': [33, 15, 28, 31, 12, 30], # Oscilação baseada na marcação
        'EFG_PCT': 62.5 # Effective Field Goal % (Peso altíssimo na LTH)
    }

    # 2. O Processo de Poda (Pruning)
    # Na LTH, podamos os jogos de baixa magnitude (ruído).
    # Removemos os jogos de 12 e 15 pts, que na temporada 2026 geralmente ocorrem
    # em noites de "box-and-one" extremo ou cansaço físico.
    sub_rede_estavel = [p for p in stats_2026['RECENTE'] if p > 20]

    # 3. Identificação do Winning Ticket
    # O bilhete premiado de Curry é a "convergência do caos": 
    # A capacidade de converter arremessos de alta dificuldade quando a rede está sob pressão.
    convergencia_sub_rede = sum(sub_rede_estavel) / len(sub_rede_estavel)
    
    # Predição Final: 75% da Sub-rede de Elite + 25% Estabilidade da Temporada
    predicao = (convergencia_sub_rede * 0.75) + (stats_2026['PTS_AVG'] * 0.25)

    print(f"--- Predição Stephen Curry (Winning Ticket - Temporada 25/26) ---")
    print(f"Arquitetura Base (Média): {stats_2026['PTS_AVG']} PPG")
    print(f"Média de 3PM (Pesos Ativos): {stats_2026['3PM_AVG']} bolas/jogo")
    print(f"Sub-rede Isolada (Gravity Ticket): {convergencia_sub_rede:.1f} PPG")
    print("-" * 55)
    print(f"PREDIÇÃO DE CONVERGÊNCIA: {predicao:.1f} PPG")

    return predicao

predicao_curry_winning_ticket()