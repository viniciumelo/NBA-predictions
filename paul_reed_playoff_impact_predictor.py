import pandas as pd
from nba_api.stats.endpoints import playercareerstats, playerdashboardbygeneralsplits
from nba_api.stats.static import players

def obter_dados_analise():
    # Localiza o ID via string matching
    player = [p for p in players.get_players() if p['full_name'] == 'Paul Reed'][0]
    player_id = player['id']
    
    # Coleta de dados da temporada regular atual (2025-26)
    # O endpoint dashboard fornece divisões granulares de estatísticas
    current_season = playerdashboardbygeneralsplits.PlayerDashboardByGeneralSplits(
        player_id=player_id, 
        season='2025-26'
    ).get_data_frames()[0]
    
    # Coleta de dados históricos de Playoffs para comparação de intensidade
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    df_playoffs_hist = career.get_data_frames()[2]
    
    return current_season, df_playoffs_hist

