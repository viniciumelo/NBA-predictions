import pandas as pd
from nba_api.stats.endpoints import playerdashboardbygeneralsplits, playercareerstats
from nba_api.stats.static import players

def get_cooper_flagg_id():
    # Busca o ID do Cooper Flagg
    player = [p for p in players.get_players() if "Cooper Flagg" in p['full_name']][0]
    return player['id']

def predict_flagg_points():
    player_id = get_cooper_flagg_id()
    
    # 1. Busca dados da temporada de calouro (2025-26)
    # Analisamos os últimos meses para ver a evolução do ritmo dele
    current_season = playerdashboardbygeneralsplits.PlayerDashboardByGeneralSplits(
        player_id=player_id,
        season='2025-26'
    ).get_data_frames()[0]
    
    if current_season.empty:
        print("Dados da temporada 2025-26 não encontrados.")
        return

    # Estatísticas atuais
    avg_pts = current_season['PTS'].iloc[0] / current_season['GP'].iloc[0]
    fg_pct = current_season['FG_PCT'].iloc[0]
    ft_pct = current_season['FT_PCT'].iloc[0]
    
    