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

    