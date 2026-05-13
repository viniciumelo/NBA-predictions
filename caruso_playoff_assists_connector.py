import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predict_caruso_assists():
    # Coleta estatísticas da temporada regular 2025-26
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        per_mode_detailed='PerGame'
    ).get_data_frames()[0]
    
    # Localizar Alex Caruso
    caruso_stats = stats[stats['PLAYER_NAME'].str.contains("Alex Caruso")]
    
    if caruso_stats.empty:
        print("Dados de Alex Caruso não encontrados. Verifique a conexão com a API.")
        return

    # Estatísticas de base
    reg_ast = caruso_stats['AST'].iloc[0]
    reg_min = caruso_stats['MIN'].iloc[0]
    reg_tov = caruso_stats['TOV'].iloc[0] # Turnovers para cálculo de ratio
    
    # --- Parâmetros de Projeção Playoff ---
    # 1. Minutos: Caruso é vital na defesa e deve jogar ~34-36 minutos em Playoffs.
    playoff_min_projection = 35.0
    
    