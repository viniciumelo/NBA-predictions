import pandas as pd
from nba_api.stats.endpoints import playercareerstats, playerdashboardbygeneralsplits
from nba_api.stats.static import players

def get_tatum_stats():
    # Localiza o ID do Jayson Tatum
    tatum = [p for p in players.get_players() if p['full_name'] == 'Jayson Tatum'][0]
    tatum_id = tatum['id']
    
    # Busca estatísticas de carreira (Regular vs Playoffs)
    career = playercareerstats.PlayerCareerStats(player_id=tatum_id)
    df_reg_career = career.get_data_frames()[0]
    df_post_career = career.get_data_frames()[2]
    
    # Busca dados da temporada atual (2025-26)
    current_season = playerdashboardbygeneralsplits.PlayerDashboardByGeneralSplits(
        player_id=tatum_id,
        season='2025-26'
    ).get_data_frames()[0]
    
    return df_reg_career, df_post_career, current_season

def predict_tatum_points():
    df_reg, df_post, current = get_tatum_stats()
    
    # Médias de Carreira (Últimos 3 anos de Playoffs são mais relevantes para o Tatum atual)
    # Filtramos apenas as últimas 3 participações em pós-temporada
    recent_playoffs_avg = df_post.tail(3)['PTS'].sum() / df_post.tail(3)['GP'].sum()
    recent_reg_avg = df_reg.tail(3)['PTS'].sum() / df_reg.tail(3)['GP'].sum()
    
    # Fator de Elevação: O quanto ele cresce como pontuador principal
    elevation_factor = recent_playoffs_avg / recent_reg_avg
    
    