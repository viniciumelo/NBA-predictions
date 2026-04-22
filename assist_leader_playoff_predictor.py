import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats
from nba_api.stats.static import players

def get_playmaker_stats():
    # Coleta estatísticas de todos os jogadores ativos em 2025-26
    stats = leaguedashplayerstats.LeagueDashPlayerStats(season='2025-26').get_data_frames()[0]
    
   