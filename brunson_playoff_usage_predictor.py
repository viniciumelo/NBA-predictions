import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predict_brunson_points():
    # Coleta estatísticas da temporada regular 2025-26
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        per_mode_detailed='PerGame'
    ).get_data_frames()[0]
    
    # Localizar Jalen Brunson
    jb_stats = stats[stats['PLAYER_NAME'].str.contains("Jalen Brunson")]
    
    if jb_stats.empty:
        print("Dados de Jalen Brunson não encontrados. Verifique a conexão com a API.")
        return

    