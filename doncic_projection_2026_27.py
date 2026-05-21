import pandas as pd
from nba_api.stats.endpoints import playercareerstats

def predict_doncic_next_season():
    # ID fixo de Luka Dončić na NBA API
    doncic_id = 1629029
    
    print("Buscando historico de carreira de Luka Doncic...")
    career = playercareerstats.PlayerCareerStats(player_id=doncic_id)
    df_totals = career.get_data_frames()[0]
    
    # Filtrar apenas temporada regular
    df_reg = df_totals[df_totals['WHEN_MADE'] == 'Regular Season'].copy()
    
    if df_reg.empty:
        df_reg = df_totals
        
    # Calcular medias por jogo historicas
    df_reg['PPG'] = df_reg['PTS'] / df_reg['GP']
    df_reg['APG'] = df_reg['AST'] / df_reg['GP']
    df_reg['RPG'] = df_reg['REB'] / df_reg['GP']
    df_reg['MPG'] = df_reg['MIN'] / df_reg['GP']
    
    # Selecionar as ultimas 3 temporadas (teto de volume e maturidade)
    recent_seasons = df_reg.tail(3)
    
    if len(recent_seasons) < 3:
        print("Dados historicos insuficientes para calcular a tendencia.")
        return

    