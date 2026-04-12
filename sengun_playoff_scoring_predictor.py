import pandas as pd
from nba_api.stats.endpoints import playercareerstats, playerdashboardbygeneralsplits
from nba_api.stats.static import players

def get_sengun_data():
    # Localiza o ID do Alperen Sengun
    sengun = [p for p in players.get_players() if p['full_name'] == 'Alperen Sengun'][0]
    sengun_id = sengun['id']
    
    # Busca histórico de carreira (Regular vs Playoffs)
    career = playercareerstats.PlayerCareerStats(player_id=sengun_id)
    df_reg_career = career.get_data_frames()[0]
    df_post_career = career.get_data_frames()[2]
    
    