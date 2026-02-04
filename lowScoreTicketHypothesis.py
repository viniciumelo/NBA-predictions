import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def encontrar_winning_ticket_low_scoring():
    print("Iniciando Poda Iterativa para isolar a sub-rede de 'Baixa Produção'...")
    
    # 1. Coleta da Rede Densa (Pool de Talentos 2025-26)
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    # 2. O Processo de Poda (Pruning)
    # Na LTH, removemos os neurônios que 'disparam' muito (alto USG% ou alto PTS).
    # Queremos isolar a sub-rede que sobrevive mesmo quando a exigência de minutos é alta.
    media_minutos = stats['MIN'].mean()
    
    # Poda: Removemos quem joga pouco (ruído) e quem tem uso de posse acima da média (estrelas)
    sub_rede = stats[
        (stats['MIN'] >= 25) & 
        (stats['USG_PCT'] < stats['USG_PCT'].median())
    ].copy()

    