import pandas as pd
from nba_api.stats.endpoints import playercareerstats

def predict_jokic_next_season():
    # ID fixo de Nikola Jokić na NBA API
    jokic_id = 203999
    
    print("Buscando histórico de carreira de Nikola Jokic...")
    career = playercareerstats.PlayerCareerStats(player_id=jokic_id)
    df_totals = career.get_data_frames()[0]
    
    # Filtrar apenas temporada regular
    df_reg = df_totals[df_totals['WHEN_MADE'] == 'Regular Season'].copy()
    
    