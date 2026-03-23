import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats
from nba_api.stats.static import teams

def get_possession_data():
    # Puxa estatísticas detalhadas de todos os times na temporada atual
    stats = leaguedashteamstats.LeagueDashTeamStats(per_mode_detailed='PerGame').get_data_frames()[0]
    
    # Selecionamos colunas relevantes para o cálculo de posse
    # FGA: Arremessos tentados, FTA: Lances livres, TOV: Turnovers, OREB: Rebotes Ofensivos
    relevant_stats = stats[['TEAM_NAME', 'TEAM_ID', 'FGA', 'FTA', 'TOV', 'OREB']]
    
    # Fórmula de Estimativa de Posses (Pace)
    relevant_stats['EST_POSSESSIONS'] = 0.96 * (
        relevant_stats['FGA'] + 
        relevant_stats['TOV'] + 
        (0.44 * relevant_stats['FTA']) - 
        relevant_stats['OREB']
    )
    
    return relevant_stats

def predict_possession_advantage(team_a_name, team_b_name):
    df = get_possession_data()
    
    team_a = df[df['TEAM_NAME'].str.contains(team_a_name, case=False)]
    team_b = df[df['TEAM_NAME'].str.contains(team_b_name, case=False)]
    
    if team_a.empty or team_b.empty:
        return "Time não encontrado. Verifique o nome."

    poss_a = team_a.iloc[0]['EST_POSSESSIONS']
    poss_b = team_b.iloc[0]['EST_POSSESSIONS']
    
    