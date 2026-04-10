import pandas as pd
from nba_api.stats.endpoints import playercareerstats, playerdashboardbygeneralsplits
from nba_api.stats.static import players

def get_ant_data():
    # Localiza o ID do Anthony Edwards
    ant = [p for p in players.get_players() if p['full_name'] == 'Anthony Edwards'][0]
    ant_id = ant['id']
    
    # Busca histórico de carreira (Regular vs Playoffs)
    career = playercareerstats.PlayerCareerStats(player_id=ant_id)
    df_reg_career = career.get_data_frames()[0]
    df_post_career = career.get_data_frames()[2]
    