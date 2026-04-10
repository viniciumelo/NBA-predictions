import pandas as pd
from nba_api.stats.endpoints import playercareerstats, playerdashboardbygeneralsplits
from nba_api.stats.static import players

def get_chet_data():
    # Localiza o ID do Chet Holmgren
    chet = [p for p in players.get_players() if p['full_name'] == 'Chet Holmgren'][0]
    chet_id = chet['id']
    
    