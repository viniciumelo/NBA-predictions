import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats

def predicao_faltas_equipe():
    print("Analisando agressividade coletiva e métricas de arbitragem...")
    
    # 1. Coletar estatísticas das equipes na temporada atual
    # Usamos MeasureType='Base' para pegar PF (Personal Fouls)
    team_stats = leaguedashteamstats.LeagueDashTeamStats(
        season='2025-26',
        measure_type_detailed_advanced='Base'
    ).get_data_frames()[0]

    # 2. Coletar métricas avançadas (Pace e Defensive Rating)
    adv_stats = leaguedashteamstats.LeagueDashTeamStats(
        season='2025-26',
        measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    # 3. Unificar dados
    df = pd.merge(team_stats, adv_stats[['TEAM_ID', 'PACE', 'DEF_RATING']], on='TEAM_ID')

    # 4. Cálculo do Foul Score
    # Valorizamos: (Faltas por jogo / Pace) * Defensive Rating
    # Times com Def Rating alto (pior defesa) tendem a fazer mais faltas para compensar
    df['TEAM_FOUL_SCORE'] = (df['PF'] / df['PACE']) * (df['DEF_RATING'] / 100)

    # Ordenar pelas equipes com maior tendência de faltas
    ranking = df[['TEAM_NAME', 'PF', 'PACE', 'DEF_RATING', 'TEAM_FOUL_SCORE']]
    ranking = ranking.sort_values(by='TEAM_FOUL_SCORE', ascending=False).head(5)

    print("\n--- EQUIPES COM MAIOR TENDÊNCIA DE COMETER FALTAS ---")
    for i, row in ranking.iterrows():
        print(f"{row['TEAM_NAME']} | Média: {row['PF']:.1f} faltas/jogo | Ritmo (Pace): {row['PACE']:.1f}")
    
    return ranking

predicao_faltas_equipe()