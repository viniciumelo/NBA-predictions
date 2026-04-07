import pandas as pd
from nba_api.stats.endpoints import playercareerstats, playerdashboardbygeneralsplits
from nba_api.stats.static import players

def get_tatum_stats():
    # Localiza o ID do Jayson Tatum
    tatum = [p for p in players.get_players() if p['full_name'] == 'Jayson Tatum'][0]
    tatum_id = tatum['id']
   