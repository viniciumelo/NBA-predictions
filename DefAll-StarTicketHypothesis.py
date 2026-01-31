import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def encontrar_winning_ticket_defensivo():
    print("Aplicando Poda Iterativa para isolar o 'Bilhete Premiado' da defesa...")

    # 1. Coleta da Rede Densa (Dados de 2025-26)
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    