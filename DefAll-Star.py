import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predicao_defesa_allstar():
    print("Analisando especialistas em 'Lockdown' para o All-Star 2026...")
    
    # 1. Coletar dados avançados da temporada 2025-26
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    # 2. Filtrar jogadores All-Star (PIE alto e minutagem)
    # Focamos em jogadores que têm Defensive Rating baixo (melhor defesa)
    all_stars = stats[stats['PIE'] > 0.14].copy()

    