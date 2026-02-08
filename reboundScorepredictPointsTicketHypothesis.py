import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def encontrar_winning_ticket_rebotes():
    print("Iniciando Poda Iterativa para isolar a sub-rede de domínio de garrafão...")
    
    # 1. Coleta da Rede Densa (Dados Avançados 2025-26)
    # Buscamos a arquitetura completa de rebotes da liga
    df = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    # 2. O Processo de Poda (Pruning)
    # Na LTH, removemos neurônios de baixa magnitude. 
    # Cortamos jogadores que não têm volume de garrafão (MIN) 
    # e aqueles cuja taxa de rebotes está abaixo da média da liga (ruído estatístico).
    poda_minutos = 20
    media_reb_pct = df['REB_PCT'].mean()
    
    sub_rede = df[
        (df['MIN'] >= poda_minutos) & 
        (df['REB_PCT'] > media_reb_pct)
    ].copy()

    # 3. Identificação do Winning Ticket (Rebound Stability Score)
    # O bilhete premiado não é apenas volume (REB), mas eficiência na sub-rede (REB_PCT)
    # Somamos o impacto defensivo (DREB_PCT) e a agressividade ofensiva (OREB_PCT)
    sub_rede['TICKET_SCORE'] = (
        (sub_rede['REB_PCT'] * 100) + 
        (sub_rede['OREB_PCT'] * 50) + 
        (sub_rede['DREB_PCT'] * 20)
    )

    # 4. Isolando os 5 Bilhetes Premiados
    winning_tickets = sub_rede.sort_values(by='TICKET_SCORE', ascending=False).head(5)

    print("\n--- WINNING TICKETS: A SUB-REDE DE DOMÍNIO DE REBOTES ---")
    for rank, (_, row) in enumerate(winning_tickets.iterrows(), 1):
        status = "💎 BILHETE DE ELITE" if rank <= 2 else "✅ SUB-REDE ESTÁVEL"
        print(f"{rank}. {row['PLAYER_NAME']} [{row['TEAM_ABBREVIATION']}]")
        print(f"   > Eficiência Total: {row['REB_PCT']:.1%} | Ticket Score: {row['TICKET_SCORE']:.2f}")
        print(f"   > Status: {status}\n")
    
    return winning_tickets
