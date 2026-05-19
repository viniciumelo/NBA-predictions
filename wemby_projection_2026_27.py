import pandas as pd
from nba_api.stats.endpoints import playercareerstats

def predict_wemby_next_season():
    # ID fixo de Victor Wembanyama na NBA API
    wemby_id = 1641705
    
    print("Buscando histórico de carreira de Victor Wembanyama...")
    career = playercareerstats.PlayerCareerStats(player_id=wemby_id)
    df_totals = career.get_data_frames()[0]
    
    # Filtrar apenas temporada regular
    df_reg = df_totals[df_totals['WHEN_MADE'] == 'Regular Season'].copy()
    
    if df_reg.empty:
        df_reg = df_totals
        
    # Calcular médias por jogo históricas
    df_reg['PPG'] = df_reg['PTS'] / df_reg['GP']
    df_reg['APG'] = df_reg['AST'] / df_reg['GP']
    df_reg['RPG'] = df_reg['REB'] / df_reg['GP']
    df_reg['BPG'] = df_reg['BLK'] / df_reg['GP']
    df_reg['MPG'] = df_reg['MIN'] / df_reg['GP']
    
    # Analisar o histórico recente de evolução
    recent_seasons = df_reg.tail(3)
    
    