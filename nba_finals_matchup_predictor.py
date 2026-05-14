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
    