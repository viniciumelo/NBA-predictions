import pandas as pd
from nba_api.stats.endpoints import playercareerstats, playerdashboardbygeneralsplits
from nba_api.stats.static import players

def get_hukporti_stats():
    # Localiza o ID do Ariel Hukporti
    player = [p for p in players.get_players() if p['full_name'] == 'Ariel Hukporti'][0]
    player_id = player['id']
    
   