import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predict_antman_performance():
    # Coleta estatísticas da temporada regular 2025-26
    # O endpoint retorna dados atualizados da liga
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        per_mode_detailed='PerGame'
    ).get_data_frames()[0]
    
    