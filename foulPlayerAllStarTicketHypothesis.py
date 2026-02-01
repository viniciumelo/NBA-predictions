import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def encontrar_bilhete_faltas_allstar():
    print("Executando poda iterativa para identificar o 'Winning Ticket' de faltas...")
    
    # 1. Coleta da Rede Densa (Pool de Talentos 2025-26)
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        measure_type_detailed_advanced='Base'
    ).get_data_frames()[0]

    # 2. Processo de Poda (Pruning)
    # Na LTH, removemos os parâmetros (jogadores) que não têm "peso" suficiente na categoria.
    # Vamos podar quem joga pouco ou tem baixo impacto, focando no núcleo All-Star.
    threshold_pie = stats['PIE'].median()
    sub_rede = stats[stats['PIE'] > threshold_pie].copy()

    # 3. Identificação do Winning Ticket (Foul Architecture)
    # Calculamos a propensão intrínseca: Faltas Cometidas vs Faltas Sofridas (Agressividade Relativa)
    # Multiplicamos pelo volume de minutos para ver a consistência do 'bilhete'.
    sub_rede['FOUL_TICKET_SCORE'] = (
        ((sub_rede['PF'] / sub_rede['MIN']) * 36 * 0.6) +  # Intensidade por minuto
        (sub_rede['STL'] * 0.2) +                          # Tentativas de roubo (risco)
        (sub_rede['BLK'] * 0.2)                            # Contestação de aro (risco)
    )

    # 4. Isolando os "Vencedores" da Loteria de Faltas
    # Ordenamos para encontrar a sub-rede mais propensa ao apito
    ranking = sub_rede.sort_values(by='FOUL_TICKET_SCORE', ascending=False).head(5)

    print("\n--- SUB-REDE IDENTIFICADA: OS 'BILHETES PREMIADOS' DO APITO ---")
    for rank, (i, row) in enumerate(ranking.iterrows(), 1):
        print(f"{rank}. {row['PLAYER_NAME']} [{row['TEAM_ABBREVIATION']}]")
        print(f"   > Score de Agressividade: {row['FOUL_TICKET_SCORE']:.2f}")
        print(f"   > Estilo: {'Protetor de Aro' if row['BLK'] > 1.5 else 'Defensor de Perímetro'}\n")
    
    return ranking
