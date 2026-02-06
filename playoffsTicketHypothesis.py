import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats

def predicao_playoffs_lottery_ticket(time_a, time_b):
    print(f"Buscando o 'Winning Ticket' para o confronto: {time_a} vs {time_b}...")

    # 1. Coleta da Rede Densa (Estatísticas de Temporada e Playoffs 2025-26)
    # Na LTH, começamos com a rede completa para identificar os pesos iniciais
    stats = leaguedashteamstats.LeagueDashTeamStats(
        season='2025-26',
        measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    