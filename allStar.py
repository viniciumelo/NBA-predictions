import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predicao_all_star_chance():
    print("Calculando probabilidades de All-Star baseadas em métricas históricas...")
    
    # 1. Coletar dados da temporada (Representando o 'Ano Anterior' ou Atual)
    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2024-25',
        measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    # 2. Coletar dados básicos para Pontos e Vitórias
    base_stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2024-25',
        measure_type_detailed_advanced='Base'
    ).get_data_frames()[0]

    # 3. Mesclar dados
    df = pd.merge(base_stats[['PLAYER_ID', 'PLAYER_NAME', 'TEAM_ABBREVIATION', 'PTS', 'W_PCT']], 
                  player_stats[['PLAYER_ID', 'PIE', 'USG_PCT']], on='PLAYER_ID')

    # 4. Cálculo da Probabilidade All-Star (%)
    # A fórmula considera: Volume de Pontos (40%), Eficiência PIE (30%), 
    # Sucesso do Time (20%) e Uso de Posse/Estrelato (10%)
    df['ALL_STAR_CHANCE'] = (
        (df['PTS'] * 2.0) +           # Pontos são o maior chamariz de votos
        (df['PIE'] * 150) +           # Impacto real no jogo
        (df['W_PCT'] * 20) +          # Times vencedores levam mais jogadores
        (df['USG_PCT'] * 50)          # Jogadores que dominam a bola são mais "vistos"
    )
