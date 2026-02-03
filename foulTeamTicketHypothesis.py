import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats

def encontrar_bilhete_premiado_faltas():
    print("Iniciando Poda Iterativa para isolar a sub-rede de agressividade coletiva...")
    
    # 1. Coleta da 'Rede Densa' (Estatísticas Base e Avançadas)
    team_base = leaguedashteamstats.LeagueDashTeamStats(
        season='2025-26', measure_type_detailed_advanced='Base'
    ).get_data_frames()[0]

    team_adv = leaguedashteamstats.LeagueDashTeamStats(
        season='2025-26', measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    df = pd.merge(team_base[['TEAM_ID', 'TEAM_NAME', 'PF', 'GP']], 
                  team_adv[['TEAM_ID', 'PACE', 'DEF_RATING', 'PCT_AST']], on='TEAM_ID')

    