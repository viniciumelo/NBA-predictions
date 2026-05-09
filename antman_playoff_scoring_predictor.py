import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predict_antman_performance():
    # Coleta estatísticas da temporada regular 2025-26
    # O endpoint retorna dados atualizados da liga
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        per_mode_detailed='PerGame'
    ).get_data_frames()[0]
    
    # Localizar Anthony Edwards
    ant_stats = stats[stats['PLAYER_NAME'].str.contains("Anthony Edwards")]
    
    if ant_stats.empty:
        print("Dados de Anthony Edwards não encontrados. Verifique a conexão com a API.")
        return

    # Estatísticas de base na temporada regular
    reg_pts = ant_stats['PTS'].iloc[0]
    reg_min = ant_stats['MIN'].iloc[0]
    reg_fga = ant_stats['FGA'].iloc[0] # Tentativas de arremesso
    
    # --- Parâmetros de Projeção Playoff (Modelo Ant-Man) ---
    # 1. Minutos: Em jogos decisivos, Ant Man tende a jogar ~41 minutos.
    playoff_min_projection = 41.0
    
    # 2. Alpha Scorer Factor: 
    # Edwards aumenta sua agressividade (FGA) em cerca de 15% nos Playoffs.
    # Aplicamos um multiplicador de eficiência ajustada de 1.15.
    alpha_boost_factor = 1.15
    
   