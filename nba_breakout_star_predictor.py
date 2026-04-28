import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predizer_revelacao_ano():
    # Coleta de dados da temporada atual (2025-26)
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        per_mode_detailed='PerGame'
    ).get_data_frames()[0]
    
    # Filtramos jogadores com menos de 3 anos de liga (critério de 'revelação')
    # e alta minutagem para filtrar amostragem insuficiente
    df = stats[(stats['MIN'] > 20.0)].copy()
    
   