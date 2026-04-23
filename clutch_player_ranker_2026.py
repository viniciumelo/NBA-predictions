import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def identificar_jogador_mais_decisivo():
    # Coleta estatísticas gerais da temporada 2025-26
    # Nota: Em um cenário real, usaríamos o endpoint 'clutchperformancedashboard'
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26', 
        measure_type_detailed_defense='Base'
    ).get_data_frames()[0]
    
    