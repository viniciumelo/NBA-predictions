import pandas as pd
from nba_api.stats.endpoints import playercareerstats, playerdashboardbygeneralsplits
from nba_api.stats.static import players

def get_booker_stats():
    # Localiza o ID do Devin Booker
    player = [p for p in players.get_players() if p['full_name'] == 'Devin Booker'][0]
    player_id = player['id']
    
   