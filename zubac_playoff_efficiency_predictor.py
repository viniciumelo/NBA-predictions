import pandas as pd
from nba_api.stats.endpoints import playercareerstats, playerdashboardbygeneralsplits
from nba_api.stats.static import players

def get_zubac_data():
    # Localiza o ID do Ivica Zubac
    player = [p for p in players.get_players() if p['full_name'] == 'Ivica Zubac'][0]
    player_id = player['id']
    
    