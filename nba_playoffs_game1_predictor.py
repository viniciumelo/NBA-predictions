import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats
from nba_api.stats.static import teams

def get_playoff_stats():
    # Puxa estatísticas avançadas (Advanced) para medir o Net Rating
    stats = leaguedashteamstats.LeagueDashTeamStats(
        measure_type_detailed_defense='Advanced',
        per_mode_detailed='PerGame'
    ).get_data_frames()[0]
    
    # Filtramos colunas essenciais: Nome, Rating Ofensivo, Defensivo e Net (Saldo)
    return stats[['TEAM_NAME', 'OFF_RATING', 'DEF_RATING', 'NET_RATING', 'W_PCT']]

def predict_game_1(home_team_name, away_team_name):
    df = get_playoff_stats()
    
    home_stats = df[df['TEAM_NAME'].str.contains(home_team_name, case=False)]
    away_stats = df[df['TEAM_NAME'].str.contains(away_team_name, case=False)]
    
    if home_stats.empty or away_stats.empty:
        print("Erro: Verifique os nomes das equipes.")
        return

    # Extração do Net Rating (Eficiência Líquida)
    home_net = home_stats.iloc[0]['NET_RATING']
    away_net = away_stats.iloc[0]['NET_RATING']
    
    # Ajuste de Vantagem em Casa (Historicamente ~ +3.0 no Net Rating na NBA)
    home_adjusted_score = home_net + 3.0
    away_adjusted_score = away_net
    
    