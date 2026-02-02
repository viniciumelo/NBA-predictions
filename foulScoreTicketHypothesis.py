import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def encontrar_winning_ticket_faltas():
    print("Iniciando Poda Iterativa para isolar a sub-rede de 'Foul Trouble'...")
    
    # 1. A Rede Densa (Pool de parâmetros da temporada 2025-26)
    df = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        measure_type_detailed_advanced='Base'
    ).get_data_frames()[0]

    