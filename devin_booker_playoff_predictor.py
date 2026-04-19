import pandas as pd
from nba_api.stats.endpoints import playercareerstats, playerdashboardbygeneralsplits
from nba_api.stats.static import players

def get_booker_stats():
    # Localiza o ID do Devin Booker
    player = [p for p in players.get_players() if p['full_name'] == 'Devin Booker'][0]
    player_id = player['id']
    
    # Dados da temporada atual (2025-26)
    current_season = playerdashboardbygeneralsplits.PlayerDashboardByGeneralSplits(
        player_id=player_id, 
        season='2025-26'
    ).get_data_frames()[0]
    
    # Histórico de Playoffs
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    df_post = career.get_data_frames()[2]
    
    return current_season, df_post

def predict_booker_points():
    try:
        current, hist = get_booker_stats()
        
        # Métricas da Temporada 2025-26
        avg_pts_reg = current['PTS'].iloc[0] / current['GP'].iloc[0]
        avg_min_reg = current['MIN'].iloc[0] / current['GP'].iloc[0]
        
        