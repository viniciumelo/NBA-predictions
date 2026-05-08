import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predict_lebron_points():
    # Coleta estatísticas da temporada regular 2025-26
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        per_mode_detailed='PerGame'
    ).get_data_frames()[0]
    
    # Localizar LeBron James
    lbj_stats = stats[stats['PLAYER_NAME'].str.contains("LeBron James")]
    
    if lbj_stats.empty:
        print("Dados de LeBron James não encontrados. Verifique se ele está ativo na temporada.")
        return
