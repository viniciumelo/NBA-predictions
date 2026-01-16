import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predicao_rebotes():
    print("Analisando presença de garrafão e eficiência de rebotes...")
    
    # 1. Coletar estatísticas avançadas da temporada
    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    # 2. Filtro: Jogadores com tempo de quadra real (Min 20 min)
    pivot_candidates = player_stats[player_stats['MIN'] >= 20].copy()

    # 3. Cálculo do Rebound Impact Score
    # REB_PCT: % de rebotes totais disponíveis que o jogador coleta
    # OreB_PCT: % de rebotes ofensivos (gera segundas chances)
    pivot_candidates['REB_IMPACT'] = (
        (pivot_candidates['REB_PCT'] * 70) + 
        (pivot_candidates['OREB_PCT'] * 30)
    )

    