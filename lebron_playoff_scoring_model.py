import pandas as pd
from nba_api.stats.endpoints import playercareerstats, playerdashboardbygeneralsplits
from nba_api.stats.static import players

def get_lebron_data():
    # Localiza o ID do LeBron James
    lbj = [p for p in players.get_players() if p['full_name'] == 'LeBron James'][0]
    lbj_id = lbj['id']
    
    