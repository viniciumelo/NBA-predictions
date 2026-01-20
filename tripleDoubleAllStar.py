import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predicao_triple_double_allstar():
    print("Analisando versatilidade para Triple-Double no All-Star...")
    
    # 1. Coletar dados da temporada atual (para ver quem está produzindo em várias áreas)
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        measure_type_detailed_advanced='Base'
    ).get_data_frames()[0]

    # 2. Filtrar jogadores que são 'Estrelas' (Média > 20 pts) 
    # e que têm médias altas de Rebotes E Assistências
    stars = stats[stats['PTS'] >= 20].copy()

    # 3. Cálculo do TD-Score (Triple Double Score)
    # A fórmula prioriza quem já chega perto do triplo-duplo na temporada regular
    # Peso: Assistências (40%) + Rebotes (40%) + Histórico de Minutos (20%)
    stars['TD_CHANCE'] = (
        (stars['AST'] * 5) + 
        (stars['REB'] * 4) + 
        (stars['PIE'] * 100) # Impacto global
    )

  