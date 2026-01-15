import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predicao_risco_faltas():
    print("Analisando agressividade defensiva e risco de faltas...")
    
    # 1. Coletar estatísticas da temporada atual
    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        measure_type_detailed_advanced='Base'
    ).get_data_frames()[0]

    # 2. Filtro: Jogadores que atuam pelo menos 15 minutos (volume real de jogo)
    jogadores_ativos = player_stats[player_stats['MIN'] >= 15].copy()

    # 3. Cálculo do Risco de Faltas (Foul Risk Score)
    # Criamos a métrica Faltas por 36 Minutos
    jogadores_ativos['PF_PER_36'] = (jogadores_ativos['PF'] / jogadores_ativos['MIN']) * 36

    # Ordenar pelos jogadores que mais cometem faltas proporcionalmente
    ranking = jogadores_ativos[['PLAYER_NAME', 'TEAM_ABBREVIATION', 'PF', 'MIN', 'PF_PER_36']]
    ranking = ranking.sort_values(by='PF_PER_36', ascending=False).head(5)

    print("\n--- JOGADORES COM MAIOR RISCO DE FOUL TROUBLE ---")
    for i, row in ranking.iterrows():
        print(f"{row['PLAYER_NAME']} ({row['TEAM_ABBREVIATION']}) | Faltas/36min: {row['PF_PER_36']:.2f}")
    
    return ranking

predicao_risco_faltas()