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

    # 2. O Processo de Poda (Pruning)
    # Na LTH, podamos jogos onde a magnitude foi artificialmente baixa.
    # Removemos o jogo de 14 pts (ruído), onde ele atuou como chamariz/facilitador.
    # O Winning Ticket de KD é a sua produção quando ele decide ser o "closer".
    sub_rede_estavel = [p for p in stats_2026['RECENTE'] if p > 20]

    # 3. Identificação do Winning Ticket (Convergência de Elite)
    # O bilhete premiado de KD é a "Imunidade à Contestação".
    # Ele converge para um valor alto devido à eficiência constante (TS%).
    convergencia_sub_rede = sum(sub_rede_estavel) / len(sub_rede_estavel)
    
    # Predição Final: 80% do Winning Ticket + 20% Média de Temporada
    # KD é mais estável que a maioria, por isso o peso maior na sub-rede de elite.
    predicao = (convergencia_sub_rede * 0.8) + (stats_2026['PTS_AVG'] * 0.2)

    print(f"--- Predição Kevin Durant (Winning Ticket - Temporada 25/26) ---")
    print(f"Arquitetura Base (Média): {stats_2026['PTS_AVG']} PPG")
    print(f"Localização: Houston Rockets (Fator Casa)")
    print(f"Sub-rede Isolada (Efficiency Ticket): {convergencia_sub_rede:.1f} PPG")
    print("-" * 55)
    print(f"PREDIÇÃO DE CONVERGÊNCIA: {predicao:.1f} PPG")

    return predicao

predicao_durant_winning_ticket()