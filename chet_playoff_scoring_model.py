import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predict_chet_performance():
    # Coleta estatísticas da temporada 2025-26
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        per_mode_detailed='PerGame'
    ).get_data_frames()[0]
    
    # Filtrar dados do Chet Holmgren
    chet_stats = stats[stats['PLAYER_NAME'].str.contains("Holmgren")]
    
    if chet_stats.empty:
        print("Dados de Chet Holmgren não encontrados.")
        return

    # Médias da Temporada Regular
    reg_pts = chet_stats['PTS'].iloc[0]
    reg_min = chet_stats['MIN'].iloc[0]
    
    