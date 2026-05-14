import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats

def predict_semifinalists():
    # Coleta estatísticas avançadas das equipes na temporada 2025-26
    print("Buscando dados avançados da NBA...")
    team_stats = leaguedashteamstats.LeagueDashTeamStats(
        season='2025-26',
        measure_type_detailed_defense='Advanced'
    ).get_data_frames()[0]

    # Selecionar colunas essenciais para a predição
    # Net Rating é o melhor indicador de domínio de uma equipe
    cols = ['TEAM_NAME', 'TEAM_ID', 'NET_RATING', 'W_PCT', 'OFF_RATING', 'DEF_RATING']
    df = team_stats[cols]

   