import pandas as pd
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players

def get_jokic_stats():
    # Busca o ID do Nikola Jokic
    jokic = [p for p in players.get_players() if p['full_name'] == 'Nikola Jokic'][0]
    jokic_id = jokic['id']
    
   