import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predict_wemby_blocks():
    # Coleta estatísticas da temporada 2025-26
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        per_mode_detailed='PerGame'
    ).get_data_frames()[0]
    
    # Filtrar dados do Wembanyama
    wemby_stats = stats[stats['PLAYER_NAME'].str.contains("Wembanyama")]
    
    if wemby_stats.empty:
        print("Dados de Wembanyama não encontrados para a temporada atual.")
        return

    # Extrair médias atuais
    avg_blocks = wemby_stats['BLK'].iloc[0]
    avg_mins = wemby_stats['MIN'].iloc[0]
    
    # Métrica de Eficiência: Tocos por Minuto
    blk_per_min = avg_blocks / avg_mins
    
    # --- Premissas de Playoff ---
    # 1. Minutos aumentam (Estrela joga mais tempo) -> Aprox 38 min
    # 2. Fator de Intensidade Defensiva (Aumento de 10% na taxa de tocos)
    playoff_mins = 38.0
    intensity_multiplier = 1.10
    
    projected_blocks_per_game = (blk_per_min * playoff_mins) * intensity_multiplier
    
    # Estimativa para uma série de 7 jogos
    total_series_blocks = projected_blocks_per_game * 7
    
    print(f"=== PREDICAÇÃO DE TOCOS: WEMBY NOS PLAYOFFS 2026 ===")
    print(f"Média Temporada Regular: {avg_blocks:.1f} BLK/G")
    print(f"Minutos Projetados (Playoffs): {playoff_mins}")
    print("-" * 45)
    print(f"PREDIÇÃO POR JOGO: {projected_blocks_per_game:.2f} tocos")
    print(f"TOTAL PROJETADO (Série de 7 jogos): {total_series_blocks:.0f} tocos")
    print("-" * 45)
    print("Nota: A predição considera o aumento da minutagem e o 'Rim Protection Impact' em séries longas.")
