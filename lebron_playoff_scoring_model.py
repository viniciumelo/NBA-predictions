import pandas as pd
from nba_api.stats.endpoints import playercareerstats, playerdashboardbygeneralsplits
from nba_api.stats.static import players

def get_lebron_data():
    # Localiza o ID do LeBron James
    lbj = [p for p in players.get_players() if p['full_name'] == 'LeBron James'][0]
    lbj_id = lbj['id']
    
    # Busca histórico de carreira (Regular vs Playoffs)
    career = playercareerstats.PlayerCareerStats(player_id=lbj_id)
    df_reg_career = career.get_data_frames()[0]
    df_post_career = career.get_data_frames()[2]
    
    