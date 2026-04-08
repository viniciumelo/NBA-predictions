import pandas as pd
from nba_api.stats.endpoints import playerdashboardbygeneralsplits, playercareerstats
from nba_api.stats.static import players

def get_cooper_flagg_id():
    # Busca o ID do Cooper Flagg
    player = [p for p in players.get_players() if "Cooper Flagg" in p['full_name']][0]
    return player['id']

