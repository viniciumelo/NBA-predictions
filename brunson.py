import pandas as pd
from nba_api.stats.endpoints import playergamelog
from sklearn.ensemble import RandomForestRegressor

# ID do Jalen Brunson: 1628973
BRUNSON_ID = '1628973'

def predict_brunson_pts():
    # 1. Obter logs da temporada 2025-26
    log = playergamelog.PlayerGameLog(player_id=BRUNSON_ID, season='2025-26')
    df = log.get_data_frames()[0]
    
    # Inverter para cronologia correta e limpar dados
    df = df.iloc[::-1].reset_index(drop=True)
    
    