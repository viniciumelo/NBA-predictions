import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predict_sga_scoring():
    # Coleta estatísticas da temporada 2025-26
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        per_mode_detailed='PerGame'
    ).get_data_frames()[0]
    
    # Localizar SGA (Shai Gilgeous-Alexander)
    sga_stats = stats[stats['PLAYER_NAME'].str.contains("Gilgeous-Alexander")]
    
    if sga_stats.empty:
        print("Dados de SGA não encontrados.")
        return

    # Dados da Temporada Regular
    reg_pts = sga_stats['PTS'].iloc[0]
    reg_min = sga_stats['MIN'].iloc[0]
    reg_fta = sga_stats['FTA'].iloc[0]  # Tentativas de Lance Livre
    
    # --- Ajustes Preditivos para Playoffs ---
    # 1. Minutos: Em playoffs, estrelas do nível de SGA jogam cerca de 40-42 min.
    playoff_min_projection = 40.5
    
    # 2. Fator de Uso (Usage): A posse de bola se concentra mais nele.
    # Aplicamos um multiplicador de 1.08 (8% de aumento na carga ofensiva).
    usage_multiplier = 1.08
    
    # Cálculo da Pontuação Projetada (Pontos por Minuto * Novos Minutos * Ajuste de Uso)
    pts_per_min = reg_pts / reg_min
    projected_pts_game = (pts_per_min * playoff_min_projection) * usage_multiplier
    
    # Projeção de total em uma série de 7 jogos
    series_total = projected_pts_game * 7
    
    