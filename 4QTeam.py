import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats

def predicao_pontos_4quarto():
    print("Analisando poder ofensivo no 4º quarto (Clutch Time)...")
    
    # 1. Coletar estatísticas das equipes apenas para o 4º Quarto
    # O parâmetro period_nullable=4 filtra apenas o último período
    stats_4q = leaguedashteamstats.LeagueDashTeamStats(
        season='2025-26',
        period_nullable=4,
        measure_type_detailed_advanced='Base'
    ).get_data_frames()[0]

    # 2. Coletar estatísticas avançadas do 4º Quarto (para ver o ritmo/Pace)
    adv_stats_4q = leaguedashteamstats.LeagueDashTeamStats(
        season='2025-26',
        period_nullable=4,
        measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    # 3. Unificar os dados
    df = pd.merge(stats_4q, adv_stats_4q[['TEAM_ID', 'PACE', 'OFF_RATING']], on='TEAM_ID')

    # 4. Cálculo da Projeção de Pontos
    # PTS = Pontos marcados no 4Q por jogo
    # PACE = Velocidade do jogo no 4Q (indica se o time corre ou gasta o relógio)
    df['PROJECAO_4Q'] = df['PTS'] 

    # Ordenar pelos times que mais pontuam no final
    ranking = df[['TEAM_NAME', 'PTS', 'PACE', 'OFF_RATING']].sort_values(by='PTS', ascending=False).head(5)

    print("\n--- TIMES MAIS EXPLOSIVOS NO 4º QUARTO ---")
    for i, row in ranking.iterrows():
        print(f"{row['TEAM_NAME']} | Média: {row['PTS']:.1f} pts | Eficiência: {row['OFF_RATING']}")
    
    return ranking