import pandas as pd
from nba_api.stats.endpoints import playercareerstats, playerdashboardbygeneralsplits
from nba_api.stats.static import players

def get_braun_data():
    # Localiza o ID do Christian Braun
    player = [p for p in players.get_players() if p['full_name'] == 'Christian Braun'][0]
    player_id = player['id']
    
    # Dados da temporada regular atual (2025-26)
    current_season = playerdashboardbygeneralsplits.PlayerDashboardByGeneralSplits(
        player_id=player_id, 
        season='2025-26'
    ).get_data_frames()[0]
    
    # Histórico de Playoffs (incluindo a campanha do título de 2023)
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    df_post = career.get_data_frames()[2]
    
    return current_season, df_post

def predict_braun_points():
    current, df_post = get_braun_data()
    
    # Métricas da Temporada 2025-26
    avg_pts_reg = current['PTS'].iloc[0] / current['GP'].iloc[0]
    fg3_pct = current['FG3_PCT'].iloc[0]
    
    