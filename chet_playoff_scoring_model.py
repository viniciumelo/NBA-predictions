import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predict_chet_performance():
    # Coleta estatísticas da temporada 2025-26
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        per_mode_detailed='PerGame'
    ).get_data_frames()[0]
    
   