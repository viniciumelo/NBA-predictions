import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predict_brunson_points():
    # Coleta estatísticas da temporada regular 2025-26
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        per_mode_detailed='PerGame'
    ).get_data_frames()[0]
    
    # Localizar Jalen Brunson
    jb_stats = stats[stats['PLAYER_NAME'].str.contains("Jalen Brunson")]
    
    if jb_stats.empty:
        print("Dados de Jalen Brunson não encontrados. Verifique a conexão com a API.")
        return

    # Estatísticas base da temporada
    reg_pts = jb_stats['PTS'].iloc[0]
    reg_min = jb_stats['MIN'].iloc[0]
    
    # --- Ajustes de Playoff: O Modelo "Knicks Engine" ---
    # 1. Minutos: Em Playoffs, Brunson raramente descansa, chegando a ~42 minutos.
    playoff_min_projection = 42.0
    
    # 2. Volume de Arremessos (Usage Jump):
    # Brunson assume a responsabilidade final e aumenta sua taxa de arremessos em ~18%.
    usage_expansion_factor = 1.18
    
    # Cálculo: (Pontos por Minuto) * (Novos Minutos) * (Fator de Volume)
    pts_per_min = reg_pts / reg_min
    projected_pts_game = (pts_per_min * playoff_min_projection) * usage_expansion_factor
    
    # Projeção para uma série de 7 jogos
    series_total = projected_pts_game * 7
    
    print(f"=== PREDICAÇÃO DE PERFORMANCE: JALEN BRUNSON (PLAYOFFS 2026) ===")
    print(f"Média Temporada Regular: {reg_pts:.1f} PTS/G")
    print(f"Minutos Projetados: {playoff_min_projection}")
    print("-" * 55)
    print(f"PONTUAÇÃO PROJETADA (PLAYOFFS): {projected_pts_game:.1f} PTS/G")
    print(f"TOTAL ESTIMADO (Série de 7 jogos): {series_total:.0f} PONTOS")
    print("-" * 55)
    print("Nota: O modelo reflete a alta dependência ofensiva do sistema dos Knicks.")

if __name__ == "__main__":
    predict_brunson_points()