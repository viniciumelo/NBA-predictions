import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predicao_faltas_allstar():
    print("Analisando perfil disciplinar para o All-Star Game...")
    
    # 1. Coletar dados da temporada (ano atual 2026)
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        measure_type_detailed_advanced='Base'
    ).get_data_frames()[0]

    # 2. Filtrar apenas os prováveis All-Stars (jogadores de alto impacto)
    # Focamos em jogadores com PIE alto e que jogam muitos minutos
    all_star_pool = stats[stats['PIE'] > 0.13].copy()

    