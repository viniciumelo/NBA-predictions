import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats

def encontrar_bilhete_vencedor_clutch():
    print("Executando poda de dados para isolar a sub-rede vencedora (4º Quarto)...")
    
    # 1. Coleta da 'Rede Densa' (Dados Base + Avançados)
    # Filtramos apenas o 4º período para remover o ruído dos quartos iniciais
    base_4q = leaguedashteamstats.LeagueDashTeamStats(
        season='2025-26', period_nullable=4, measure_type_detailed_advanced='Base'
    ).get_data_frames()[0]

    adv_4q = leaguedashteamstats.LeagueDashTeamStats(
        season='2025-26', period_nullable=4, measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    # Unificação focada em métricas de intensidade
    df = pd.merge(base_4q, adv_4q[['TEAM_ID', 'PACE', 'OFF_RATING', 'TS_PCT']], on='TEAM_ID')

   