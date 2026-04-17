import pandas as pd
from nba_api.stats.endpoints import playercareerstats, playerdashboardbygeneralsplits
from nba_api.stats.static import players

def get_zubac_data():
    # Localiza o ID do Ivica Zubac
    player = [p for p in players.get_players() if p['full_name'] == 'Ivica Zubac'][0]
    player_id = player['id']
    
    # Dados da temporada regular atual (2025-26)
    current_season = playerdashboardbygeneralsplits.PlayerDashboardByGeneralSplits(
        player_id=player_id, 
        season='2025-26'
    ).get_data_frames()[0]
    
    # Histórico de Playoffs (Zubac tem vasta experiência em pós-temporada)
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    df_post = career.get_data_frames()[2]
    
    return current_season, df_post

def predict_zubac_points():
    current, df_post = get_zubac_data()
    
    