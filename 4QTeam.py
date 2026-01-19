import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats

def predicao_pontos_4quarto():
    print("Analisando poder ofensivo no 4º quarto (Clutch Time)...")
    
    # 1. Coletar estatísticas das equipes apenas para o 4º Quarto
    # O parâmetro period_nullable=4 filtra apenas o último período
    stats_4q = leaguedashteamstats.LeagueDashTeamStats(
        season='2025-26',
        period_nullable=4,
        measure_type_detailed_advanced='Base'
    ).get_data_frames()[0]

    # 2. Coletar estatísticas avançadas do 4º Quarto (para ver o ritmo/Pace)
    adv_stats_4q = leaguedashteamstats.LeagueDashTeamStats(
        season='2025-26',
        period_nullable=4,
        measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    