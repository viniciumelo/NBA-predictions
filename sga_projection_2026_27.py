import pandas as pd
from nba_api.stats.endpoints import playercareerstats

def predict_sga_next_season():
    # ID fixo do Shai Gilgeous-Alexander na NBA API
    sga_id = 1628983
    
    print("Buscando histórico de carreira de SGA...")
    career = playercareerstats.PlayerCareerStats(player_id=sga_id)
    df_totals = career.get_data_frames()[0]
    
    # Filtrar apenas temporada regular
    df_reg = df_totals[df_totals['WHEN_MADE'] == 'Regular Season'].copy()
    
    