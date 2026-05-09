import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predict_antman_performance():
    # Coleta estatísticas da temporada regular 2025-26
    # O endpoint retorna dados atualizados da liga
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        per_mode_detailed='PerGame'
    ).get_data_frames()[0]
    
    # Localizar Anthony Edwards
    ant_stats = stats[stats['PLAYER_NAME'].str.contains("Anthony Edwards")]
    
    if ant_stats.empty:
        print("Dados de Anthony Edwards não encontrados. Verifique a conexão com a API.")
        return

   