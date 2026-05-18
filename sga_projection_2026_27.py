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
    
    if df_reg.empty:
        # Alternativa caso o filtro mude na API
        df_reg = df_totals
        
    # Calcular médias por jogo históricas
    df_reg['PPG'] = df_reg['PTS'] / df_reg['GP']
    df_reg['APG'] = df_reg['AST'] / df_reg['GP']
    df_reg['RPG'] = df_reg['REB'] / df_reg['GP']
    df_reg['MPG'] = df_reg['MIN'] / df_reg['GP']
    
    # Pegar as últimas 3 temporadas para analisar a tendência recente de elite
    recent_seasons = df_reg.tail(3)
    
    if len(recent_seasons) < 3:
        print("Dados históricos insuficientes para calcular a tendência.")
        return

    # Pesos para a média móvel (dando mais importância para a consistência mais recente)
    weights = [0.2, 0.3, 0.5]
    
   