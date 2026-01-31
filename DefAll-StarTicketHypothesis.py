import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def encontrar_winning_ticket_defensivo():
    print("Aplicando Poda Iterativa para isolar o 'Bilhete Premiado' da defesa...")

    # 1. Coleta da Rede Densa (Dados de 2025-26)
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    # 2. O Processo de Poda (Pruning)
    # Na LTH, removemos os 'neurônios' (jogadores) que não atingem a magnitude mínima
    # Jogadores que jogam pouco ou têm impacto defensivo passivo são podados.
    media_def_rating = stats['DEF_RATING'].mean()
    poda_threshold = stats['MIN'].median()

    # Mantemos apenas quem joga minutos relevantes e está acima da média defensiva
    sub_rede = stats[
        (stats['MIN'] >= poda_threshold) & 
        (stats['DEF_RATING'] < media_def_rating) # Menor é melhor em DEF_RATING
    ].copy()

    # 3. Identificação do Winning Ticket
    # O bilhete premiado não é apenas quem rouba bola, mas quem tem a "arquitetura" estável
    # DWS = Defensive Win Shares (Vitórias atribuídas à defesa)
    sub_rede['WINNING_TICKET_SCORE'] = (
        ((200 - sub_rede['DEF_RATING']) * 0.4) + # Estabilidade da rede
        (sub_rede['DWS'] * 50) +                # Contribuição real para a vitória
        (sub_rede['DEF_WS'] * 10)               # Eficiência defensiva pura
    )

    # 4. Resultado Final (Os 5 Bilhetes de Loteria da Defesa)
    ranking = sub_rede.sort_values(by='WINNING_TICKET_SCORE', ascending=False).head(5)

    print("\n--- SUB-REDE ISOLADA: OS LOCKDOWNS DO ALL-STAR 2026 ---")
    for _, row in ranking.iterrows():
        print(f"Bilhete Identificado: {row['PLAYER_NAME']} ({row['TEAM_ABBREVIATION']})")
        print(f" > Score de Estabilidade: {row['WINNING_TICKET_SCORE']:.2f}")
        print(f" > Impacto no Winning Share: {row['DWS']:.3f}\n")
    
    return ranking