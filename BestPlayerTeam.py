import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predicao_melhor_por_time():
    # 1. Buscar estatísticas de todos os jogadores da temporada atual
    print("Analisando impacto de todos os jogadores da liga...")
    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26', # Ajustado para o ano atual
        measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    # 2. Limpeza e Filtro
    # Consideramos apenas jogadores que jogam pelo menos 20 minutos para evitar anomalias
    stats_filtradas = player_stats[player_stats['MIN'] >= 20].copy()

    # 3. Identificar o melhor por time usando o PIE (Player Impact Estimate)
    # O PIE mede a fatia de eventos positivos que o jogador causou no jogo
    melhores_por_time = stats_filtradas.sort_values('PIE', ascending=False).drop_duplicates('TEAM_ABBREVIATION')

    # 4. Formatação do Resultado
    ranking = melhores_por_time[['TEAM_ABBREVIATION', 'PLAYER_NAME', 'PIE', 'PTS', 'AST', 'REB']]
    ranking = ranking.sort_values('TEAM_ABBREVIATION')

    print("\n--- LÍDERES DE IMPACTO POR TIME ---")
    for index, row in ranking.iterrows():
        print(f"[{row['TEAM_ABBREVIATION']}] {row['PLAYER_NAME']} | Impacto (PIE): {row['PIE']:.1%}")
    
    return ranking
