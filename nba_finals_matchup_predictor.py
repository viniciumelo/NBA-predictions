import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats

def predict_nba_finalists():
    # Coleta de dados avançados da temporada 2025-26
    print("Analisando métricas de elite para as Finais...")
    team_stats = leaguedashteamstats.LeagueDashTeamStats(
        season='2025-26',
        measure_type_detailed_defense='Advanced'
    ).get_data_frames()[0]

    # Métricas cruciais para Finalistas: 
    # Net Rating (Domínio) e PIE (Impacto Global)
    cols = ['TEAM_NAME', 'NET_RATING', 'PIE', 'W_PCT', 'TS_PCT']
    df = team_stats[cols]

    # Mapeamento de Conferências
    east_teams = [
        "Boston Celtics", "Milwaukee Bucks", "New York Knicks", "Philadelphia 76ers",
        "Cleveland Cavaliers", "Indiana Pacers", "Orlando Magic", "Miami Heat",
        "Atlanta Hawks", "Brooklyn Nets", "Chicago Bulls", "Charlotte Hornets",
        "Detroit Pistons", "Toronto Raptors", "Washington Wizards"
    ]
    
    df['CONFERENCE'] = df['TEAM_NAME'].apply(lambda x: 'East' if x in east_teams else 'West')

    # O "Finalist Score" combina Net Rating com eficiência de arremesso (True Shooting)
    # Times que não conseguem pontuar com eficiência sob pressão não chegam às Finais.
    df['FINALIST_SCORE'] = (df['NET_RATING'] * 0.7) + (df['PIE'] * 100 * 0.3)

    print("\n" + "="*65)
    print("PREDIÇÃO DO CONFRONTO DAS FINAIS DA NBA 2026")
    print("="*65)

    finalists = []

    for conf in ['East', 'West']:
        # O melhor do ranking de cada conferência é o projetado para a Final
        top_team = df[df['CONFERENCE'] == conf].sort_values(by='FINALIST_SCORE', ascending=False).iloc[0]
        finalists.append(top_team)
        
        print(f"CAMPEÃO DO {conf.upper()}: {top_team['TEAM_NAME']}")
        print(f"└─ Score de Elite: {top_team['FINALIST_SCORE']:.2f} | Win %: {top_team['W_PCT']:.3f}")

   