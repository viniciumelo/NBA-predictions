import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predicao_especialista_3pts():
    print("Analisando métricas de arremessadores de elite...")
    
    # 1. Coletar dados da temporada atual
    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        measure_type_detailed_advanced='Base'
    ).get_data_frames()[0]

    # 2. Filtrar jogadores com volume mínimo (pelo menos 4 tentativas de 3pts por jogo)
    # Isso evita jogadores que acertaram 1 de 1 e ficaram com 100% de aproveitamento
    atiradores = player_stats[player_stats['FG3A'] >= 4].copy()

    # 3. Cálculo da Probabilidade (3PT Score)
    # Valorizamos: (Média de acertos * 0.6) + (Aproveitamento % * 0.4)
    atiradores['SHARPSHOOTER_SCORE'] = (
        (atiradores['FG3M'] * 0.6) + 
        (atiradores['FG3_PCT'] * 10) # Multiplicado por 10 para normalizar o peso
    )

    # Ordenar pelos maiores scores
    ranking = atiradores[['PLAYER_NAME', 'TEAM_ABBREVIATION', 'FG3M', 'FG3A', 'FG3_PCT', 'SHARPSHOOTER_SCORE']]
    ranking = ranking.sort_values(by='SHARPSHOOTER_SCORE', ascending=False).head(5)

    print("\n--- TOP 5 JOGADORES COM MAIOR CHANCE DE CESTAS DE 3 ---")
    for i, row in ranking.iterrows():
        print(f"{row['PLAYER_NAME']} ({row['TEAM_ABBREVIATION']}) | Médias: {row['FG3M']} acertos / {row['FG3A']} tentativas ({row['FG3_PCT']:.1%})")
    
    return ranking

