import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def analisar_piores_passadores():
    # Coleta de dados
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        per_mode_detailed='PerGame'
    ).get_data_frames()[0]
    
    # Critério Acadêmico: 
    # Filtramos apenas jogadores com alta minutagem (> 25 min/jogo).
    # Jogadores que jogam muito mas distribuem pouco jogo têm o menor impacto de assistência.
    df = stats[stats['MIN'] > 25.0].copy()
    
    # Cálculo de Assistências por Minuto (Métrica de eficiência de distribuição)
    df['AST_PER_MIN'] = df['AST'] / df['MIN']
    
    