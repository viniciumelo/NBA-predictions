import pandas as pd
from nba_api.stats.endpoints import playercareerstats, playerdashboardbygeneralsplits
from nba_api.stats.static import players

def get_kd_stats():
    # Localiza o ID do Kevin Durant
    kd = [p for p in players.get_players() if p['full_name'] == 'Kevin Durant'][0]
    kd_id = kd['id']
    
    # Busca estatísticas de carreira (Regular vs Playoffs)
    career = playercareerstats.PlayerCareerStats(player_id=kd_id)
    df_reg_career = career.get_data_frames()[0]
    df_post_career = career.get_data_frames()[2]
    
    