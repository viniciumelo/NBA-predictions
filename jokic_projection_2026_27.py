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
    
    if df_reg.empty:
        df_reg = df_totals
        
    # Calcular médias por jogo históricas
    df_reg['PPG'] = df_reg['PTS'] / df_reg['GP']
    df_reg['APG'] = df_reg['AST'] / df_reg['GP']
    df_reg['RPG'] = df_reg['REB'] / df_reg['GP']
    df_reg['MPG'] = df_reg['MIN'] / df_reg['GP']
    
    # Pegar as últimas 3 temporadas para analisar o "padrão MVP" recente
    recent_seasons = df_reg.tail(3)
    
    if len(recent_seasons) < 3:
        print("Dados históricos insuficientes para calcular a tendência.")
        return

    