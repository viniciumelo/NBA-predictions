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
    
    # Busca dados da temporada atual (2025-26)
    current_season = playerdashboardbygeneralsplits.PlayerDashboardByGeneralSplits(
        player_id=kd_id,
        season='2025-26'
    ).get_data_frames()[0]
    
    return df_reg_career, df_post_career, current_season

def predict_kd_points():
    df_reg, df_post, current = get_kd_stats()
    
    # Médias de Carreira
    reg_avg = df_reg['PTS'].sum() / df_reg['GP'].sum()
    post_avg = df_post['PTS'].sum() / df_post['GP'].sum()
    
    