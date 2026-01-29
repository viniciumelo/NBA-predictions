import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def encontrar_winning_tickets_por_time():
    print("Iniciando Poda Iterativa para encontrar o 'Bilhete Premiado' de cada franquia...")
    
    # 1. Coleta da Rede Densa (Todos os jogadores da temporada 2025-26)
    all_players = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    # 2. Processo de Poda (Pruning)
    # Na LTH, removemos os 'pesos' de baixa magnitude que não contribuem para o aprendizado.
    # Filtramos jogadores com volume de jogo (MIN) e uso de posse (USG_PCT) abaixo da média.
    threshold_min = 20
    threshold_usg = all_players['USG_PCT'].mean()
    
    # Aplicando a poda: jogadores que não 'carregam' o jogo são removidos
    sub_rede = all_players[
        (all_players['MIN'] >= threshold_min) & 
        (all_players['USG_PCT'] >= threshold_usg)
    ].copy()

    # 3. Identificação do Winning Ticket (O núcleo de maior impacto)
    # Calculamos o 'Ticket Score' combinando PIE (Impacto) e Net Rating (Eficiência do time com ele)
    sub_rede['TICKET_SCORE'] = (sub_rede['PIE'] * 0.7) + (sub_rede['NET_RATING'] * 0.01)

    # Isolamos o maior score de cada time (o vencedor da loteria estatística)
    winning_tickets = sub_rede.sort_values('TICKET_SCORE', ascending=False).drop_duplicates('TEAM_ABBREVIATION')
    
    # Ordenar por sigla do time para clareza
    ranking = winning_tickets[['TEAM_ABBREVIATION', 'PLAYER_NAME', 'PIE', 'USG_PCT', 'TICKET_SCORE']]
    ranking = ranking.sort_values('TEAM_ABBREVIATION')

    print("\n--- WINNING TICKETS IDENTIFICADOS POR TIME (2025-26) ---")
    print("Esses jogadores representam a sub-rede essencial de cada equipe.\n")
    
    for _, row in ranking.iterrows():
        print(f"[{row['TEAM_ABBREVIATION']}] {row['PLAYER_NAME']}")
        print(f"   > Impacto Isolado (PIE): {row['PIE']:.1%}")
        print(f"   > Densidade de Uso (USG): {row['USG_PCT']:.1%}")
        print("-" * 40)
    
    return ranking
