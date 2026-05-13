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
    
    # 2. Connector Factor:
    # Em Playoffs, a bola circula mais para fugir de dobras.
    # Caruso atua como o "segundo passador", o que eleva suas assistências em ~12%.
    connector_boost = 1.12
    
    # Cálculo: (Assistências por Minuto) * (Minutos Projetados) * (Fator Conector)
    ast_per_min = reg_ast / reg_min
    projected_ast_game = (ast_per_min * playoff_min_projection) * connector_boost
    
    # Razão Assistência/Turnover Projetada
    ast_tov_ratio = projected_ast_game / reg_tov
    
    print(f"=== PREDICAÇÃO DE PLAYMAKING: ALEX CARUSO (PLAYOFFS 2026) ===")
    print(f"Média Assistências (Regular): {reg_ast:.1f} AST/G")
    print("-" * 55)
    print(f"MINUTOS PROJETADOS: {playoff_min_projection}")
    print(f"ASSISTÊNCIAS PROJETADAS: {projected_ast_game:.1f} AST/G")
    print(f"RATIO AST/TOV ESTIMADO: {ast_tov_ratio:.2f}")
    print("-" * 55)
    print("Nota: O modelo assume que o aumento de tempo em quadra por")
    print("necessidade defensiva gera mais oportunidades de passe extra.")
