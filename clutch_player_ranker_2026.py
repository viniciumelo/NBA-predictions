import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def identificar_jogador_mais_decisivo():
    # Coleta estatísticas gerais da temporada 2025-26
    # Nota: Em um cenário real, usaríamos o endpoint 'clutchperformancedashboard'
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26', 
        measure_type_detailed_defense='Base'
    ).get_data_frames()[0]
    
    # Filtramos jogadores com alto volume de minutos em jogos competitivos
    # O "Clutch Factor" será um cálculo ponderado de Pontos em Clutch + FG% em Clutch
    # Como uma simplificação, filtramos jogadores de elite por Impacto
    df_clutch = stats[stats['MIN'] > 1000].copy()
    
    # Criamos um índice hipotético de decisividade:
    # Índice = (Pontos por Jogo * 0.4) + (Aproveitamento FG * 0.6)
    df_clutch['DECISIVIDADE_SCORE'] = (df_clutch['PTS'] * 0.4) + (df_clutch['FG_PCT'] * 100 * 0.6)
    
    # Ordenamos pelos melhores
    rank = df_clutch.sort_values(by='DECISIVIDADE_SCORE', ascending=False).head(5)
    
    