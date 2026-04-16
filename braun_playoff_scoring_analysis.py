import pandas as pd
from nba_api.stats.endpoints import playercareerstats, playerdashboardbygeneralsplits
from nba_api.stats.static import players

def get_braun_data():
    # Localiza o ID do Christian Braun
    player = [p for p in players.get_players() if p['full_name'] == 'Christian Braun'][0]
    player_id = player['id']
    
   