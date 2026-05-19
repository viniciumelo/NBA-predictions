import pandas as pd
from nba_api.stats.endpoints import playercareerstats

def predict_wemby_next_season():
    # ID fixo de Victor Wembanyama na NBA API
    wemby_id = 1641705
    
    print("Buscando histórico de carreira de Victor Wembanyama...")
    career = playercareerstats.PlayerCareerStats(player_id=wemby_id)
    df_totals = career.get_data_frames()[0]
    
    