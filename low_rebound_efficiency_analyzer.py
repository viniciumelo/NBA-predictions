import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def analisar_piores_reboteiros():
    # Coleta de dados da temporada 2025-26
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        per_mode_detailed='PerGame'
    ).get_data_frames()[0]
    
    # Filtro: Jogadores de alta minutagem (> 25 min/jogo)
    # Jogadores que jogam muito e pegam poucos rebotes são os "menos influentes" no vidro
    df = stats[stats['MIN'] > 25.0].copy()
    
    # Cálculo de Rebotes por Minuto (Métrica de eficiência)
    df['REB_PER_MIN'] = df['REB'] / df['MIN']
    
    