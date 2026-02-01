import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def encontrar_bilhete_faltas_allstar():
    print("Executando poda iterativa para identificar o 'Winning Ticket' de faltas...")
    
    # 1. Coleta da Rede Densa (Pool de Talentos 2025-26)
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        measure_type_detailed_advanced='Base'
    ).get_data_frames()[0]
