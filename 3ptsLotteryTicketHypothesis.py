import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def encontrar_bilhete_premiado_nba():
    print("Iniciando busca pelo 'Bilhete de Loteria' (Atiradores de Elite)...")
    
    # 1. Coleta de dados (A 'Rede Inicial')
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        measure_type_detailed_advanced='Base'
    ).get_data_frames()[0]

   