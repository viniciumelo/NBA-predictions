import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predict_wemby_blocks():
    # Coleta estatísticas da temporada 2025-26
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        per_mode_detailed='PerGame'
    ).get_data_frames()[0]
    
    # Filtrar dados do Wembanyama
    wemby_stats = stats[stats['PLAYER_NAME'].str.contains("Wembanyama")]
    
    if wemby_stats.empty:
        print("Dados de Wembanyama não encontrados para a temporada atual.")
        return

    # Extrair médias atuais
    avg_blocks = wemby_stats['BLK'].iloc[0]
    avg_mins = wemby_stats['MIN'].iloc[0]
    
    # Métrica de Eficiência: Tocos por Minuto
    blk_per_min = avg_blocks / avg_mins
    
   