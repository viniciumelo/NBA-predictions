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
    
    # Busca dados da temporada atual (2025-26)
    current_season = playerdashboardbygeneralsplits.PlayerDashboardByGeneralSplits(
        player_id=sengun_id,
        season='2025-26'
    ).get_data_frames()[0]
    
    return df_reg_career, df_post_career, current_season

def predict_sengun_points():
    df_reg, df_post, current = get_sengun_data()
    
    # Média da temporada atual 2025-26
    current_ppg = current['PTS'].iloc[0] / current['GP'].iloc[0]
    current_ft_pct = current['FT_PCT'].iloc[0]
    
    # Fator de Ajuste para Pivôs Técnicos:
    # Sengun tende a jogar mais minutos nos playoffs. 
    # Se ele não tiver histórico vasto de playoffs, usamos um multiplicador de volume de 1.10 (10% a mais).
    if not df_post.empty:
        playoff_factor = (df_post['PTS'].sum() / df_post['GP'].sum()) / (df_reg['PTS'].sum() / df_reg['GP'].sum())
    else:
        playoff_factor = 1.10 
    