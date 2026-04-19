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
        
        # Fator de Playoff: Booker costuma aumentar o volume (FGA) nos playoffs
        if not hist.empty:
            recent_post = hist.tail(3) # Foca nas últimas 3 temporadas
            post_avg = recent_post['PTS'].sum() / recent_post['GP'].sum()
            playoff_factor = post_avg / (hist['PTS'].sum() / hist['GP'].sum())
        else:
            playoff_factor = 1.05 # Estimativa de aumento de volume
            
        # O modelo aplica uma projeção de minutos: Estrelas como Booker
        # tendem a jogar cerca de 38-40 minutos em jogos de playoff.
        projected_min = 39.0
        points_per_minute = avg_pts_reg / avg_min_reg
        
        