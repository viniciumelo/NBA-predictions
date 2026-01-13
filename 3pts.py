import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predicao_especialista_3pts():
    print("Analisando métricas de arremessadores de elite...")
    
    # 1. Coletar dados da temporada atual
    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        measure_type_detailed_advanced='Base'
    ).get_data_frames()[0]

    # 2. Filtrar jogadores com volume mínimo (pelo menos 4 tentativas de 3pts por jogo)
    # Isso evita jogadores que acertaram 1 de 1 e ficaram com 100% de aproveitamento
    atiradores = player_stats[player_stats['FG3A'] >= 4].copy()

    