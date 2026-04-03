import pandas as pd
from nba_api.stats.endpoints import playercareerstats, playerdashboardbygeneralsplits
from nba_api.stats.static import players
import time

def get_sga_prediction_data():
    # Busca o ID do Shai
    sga = [p for p in players.get_players() if p['full_name'] == 'Shai Gilgeous-Alexander'][0]
    sga_id = sga['id']
    
    
