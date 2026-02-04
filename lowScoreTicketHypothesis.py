import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def encontrar_winning_ticket_low_scoring():
    print("Iniciando Poda Iterativa para isolar a sub-rede de 'Baixa Produção'...")
    
    # 1. Coleta da Rede Densa (Pool de Talentos 2025-26)
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    