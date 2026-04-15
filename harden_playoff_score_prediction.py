import pandas as pd
from nba_api.stats.endpoints import playercareerstats, playerdashboardbygeneralsplits
from nba_api.stats.static import players

def get_harden_data():
    # Localiza o ID do James Harden
    harden = [p for p in players.get_players() if p['full_name'] == 'James Harden'][0]
    harden_id = harden['id']
    
    # Busca estatísticas de carreira (Regular vs Playoffs)
    career = playercareerstats.PlayerCareerStats(player_id=harden_id)
    df_reg_career = career.get_data_frames()[0]
    df_post_career = career.get_data_frames()[2]
    
    # Busca dados da temporada atual (2025-26)
    current_season = playerdashboardbygeneralsplits.PlayerDashboardByGeneralSplits(
        player_id=harden_id,
        season='2025-26'
    ).get_data_frames()[0]
    
    return df_reg_career, df_post_career, current_season

def predict_harden_points():
    df_reg, df_post, current = get_harden_data()
    
    # Médias de Carreira (Histórico de 'Playoff Harden')
    # Historicamente, Harden tem médias de 24.0 (Reg) vs 22.5 (Playoffs)
    career_reg_avg = df_reg['PTS'].sum() / df_reg['GP'].sum()
    career_post_avg = df_post['PTS'].sum() / df_post['GP'].sum()
    
    # Fator de Ajuste de Playoff (Ratio histórico)
    # Geralmente em torno de 0.93 para o Harden
    playoff_adjustment = career_post_avg / career_reg_avg
    
    # Dados da temporada 2025-26 (Média de ~23.6 PTS)
    current_ppg = current['PTS'].iloc[0] / current['GP'].iloc[0]
    current_ft_pct = current['FT_PCT'].iloc[0]
    
    # Predição baseada na média atual ajustada pelo comportamento histórico em playoffs
    # Em 2026, ele joga mais como 'Point Guard', então o teto depende dos lances livres
    predicted_points = current_ppg * playoff_adjustment
    
    