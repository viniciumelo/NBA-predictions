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

    