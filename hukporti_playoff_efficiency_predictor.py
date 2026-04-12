import pandas as pd
from nba_api.stats.endpoints import playercareerstats, playerdashboardbygeneralsplits
from nba_api.stats.static import players

def get_hukporti_stats():
    # Localiza o ID do Ariel Hukporti
    player = [p for p in players.get_players() if p['full_name'] == 'Ariel Hukporti'][0]
    player_id = player['id']
    
    # Busca dados da temporada atual (2025-26)
    current_season = playerdashboardbygeneralsplits.PlayerDashboardByGeneralSplits(
        player_id=player_id, 
        season='2025-26'
    ).get_data_frames()[0]
    
    # Busca histórico de playoffs (se houver de 2025)
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    df_post = career.get_data_frames()[2]
    
    return current_season, df_post

def predict_points():
    current, df_post = get_hukporti_stats()
    
    # Estatísticas Base 2026
    gp = current['GP'].iloc[0]
    pts = current['PTS'].iloc[0]
    mins = current['MIN'].iloc[0]
    
    # Cálculo de Eficiência: Pontos por Minuto (PPM)
    ppm = pts / mins
    
    # Projeção de minutos em Playoffs (Cenário Realista: 3 a 5 minutos)
    playoff_minutes_low = 2.0
    playoff_minutes_high = 6.0
    
    # Predição
    pred_low = playoff_minutes_low * ppm
    pred_high = playoff_minutes_high * ppm
    
    