import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def encontrar_winning_tickets_por_time():
    print("Iniciando Poda Iterativa para encontrar o 'Bilhete Premiado' de cada franquia...")
    
    # 1. Coleta da Rede Densa (Todos os jogadores da temporada 2025-26)
    all_players = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    