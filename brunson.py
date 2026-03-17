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
    
    # 2. Engenharia de Features Específicas para Pontuadores
    # Médias móveis (tendência recente)
    df['MA3_PTS'] = df['PTS'].rolling(window=3).mean()
    df['MA10_PTS'] = df['PTS'].rolling(window=10).mean()
    
    # Volume de arremessos (importante para o Brunson)
    df['FGA_LAST_5'] = df['FGA'].rolling(window=5).mean()
    
    