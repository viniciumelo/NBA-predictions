import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predict_rebound_leader():
    # Coleta estatísticas da temporada atual
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        per_mode_detailed='PerGame'
    ).get_data_frames()[0]
    