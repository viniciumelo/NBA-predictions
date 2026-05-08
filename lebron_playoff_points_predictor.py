import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predict_lebron_points():
    # Coleta estatísticas da temporada regular 2025-26
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        per_mode_detailed='PerGame'
    ).get_data_frames()[0]
    
    # Localizar LeBron James
    lbj_stats = stats[stats['PLAYER_NAME'].str.contains("LeBron James")]
    
    if lbj_stats.empty:
        print("Dados de LeBron James não encontrados. Verifique se ele está ativo na temporada.")
        return

    # Estatísticas Base
    reg_pts = lbj_stats['PTS'].iloc[0]
    reg_min = lbj_stats['MIN'].iloc[0]
    
    # --- Ajustes Preditivos: O "Modo Playoff" ---
    # 1. Minutos: Na temporada ele preserva o corpo, nos Playoffs o teto sobe.
    playoff_min_projection = 39.0
    
    # 2. Fator de Intensidade (Efficiency Bump):
    # LeBron costuma aumentar sua eficiência e volume de chutes convertidos.
    # Aplicamos um multiplicador de 1.12 (12% de aumento no impacto ofensivo).
    playoff_intensity_factor = 1.12
    
    # Cálculo: (Pontos por Minuto na temporada) * (Minutos de Playoff) * (Fator de Intensidade)
    pts_per_min = reg_pts / reg_min
    projected_pts_game = (pts_per_min * playoff_min_projection) * playoff_intensity_factor
    
    # Projeção para uma série de 7 jogos
    series_total = projected_pts_game * 7
    
    print(f"=== PREDICAÇÃO DE PERFORMANCE: LEBRON JAMES (PLAYOFFS 2026) ===")
    print(f"Média Temporada Regular: {reg_pts:.1f} PTS/G")
    print(f"Minutos Projetados: {playoff_min_projection}")
    print("-" * 55)
    print(f"PONTUAÇÃO PROJETADA (PLAYOFFS): {projected_pts_game:.1f} PTS/G")
    print(f"TOTAL ESTIMADO (Série de 7 jogos): {series_total:.0f} PONTOS")
    print("-" * 55)
    print("Nota: O modelo considera o aumento histórico de uso e minutagem do atleta.")
