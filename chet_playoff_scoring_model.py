import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predict_chet_performance():
    # Coleta estatísticas da temporada 2025-26
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        per_mode_detailed='PerGame'
    ).get_data_frames()[0]
    
    # Filtrar dados do Chet Holmgren
    chet_stats = stats[stats['PLAYER_NAME'].str.contains("Holmgren")]
    
    if chet_stats.empty:
        print("Dados de Chet Holmgren não encontrados.")
        return

    # Médias da Temporada Regular
    reg_pts = chet_stats['PTS'].iloc[0]
    reg_min = chet_stats['MIN'].iloc[0]
    
    # --- Premissas de Playoff ---
    # 1. Minutos: Em playoffs, Chet deve subir de ~30-32 para ~37 min.
    playoff_mins = 37.0
    
    # 2. Shooting Volume: O sistema do OKC distribui bem a bola, 
    # mas a eficiência do Chet (TS%) costuma se manter estável.
    # Aplicamos um multiplicador de 'Floor Spacer' de 1.05.
    spacing_multiplier = 1.05
    
    # Cálculo: (Pontos por Minuto) * (Minutos de Playoff) * (Ajuste de Sistema)
    pts_per_min = reg_pts / reg_min
    projected_pts_game = (pts_per_min * playoff_mins) * spacing_multiplier
    
    # Estimativa para uma série de 7 jogos
    series_total = projected_pts_game * 7
    
    print(f"=== PREDICAÇÃO DE PONTOS: CHET HOLMGREN (PLAYOFFS 2026) ===")
    print(f"Média Atual (Temporada): {reg_pts:.1f} PTS/G")
    print(f"Minutos Projetados: {playoff_mins}")
    print("-" * 50)
    print(f"PONTUAÇÃO PROJETADA: {projected_pts_game:.1f} PTS/G")
    print(f"TOTAL NA SÉRIE (7 JOGOS): {series_total:.0f} PONTOS")
    print("-" * 50)
    print("Nota: A projeção considera o papel de Chet como espaçador de quadra")
    print("e o aumento de volume ofensivo em rotações mais curtas.")

