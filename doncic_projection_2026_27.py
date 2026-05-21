import pandas as pd
from nba_api.stats.endpoints import playercareerstats

def predict_doncic_next_season():
    # ID fixo de Luka Dončić na NBA API
    doncic_id = 1629029
    
    print("Buscando historico de carreira de Luka Doncic...")
    career = playercareerstats.PlayerCareerStats(player_id=doncic_id)
    df_totals = career.get_data_frames()[0]
    
   