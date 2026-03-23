import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats
from nba_api.stats.static import teams

def get_possession_data():
    # Puxa estatísticas detalhadas de todos os times na temporada atual
    stats = leaguedashteamstats.LeagueDashTeamStats(per_mode_detailed='PerGame').get_data_frames()[0]
    
    # Selecionamos colunas relevantes para o cálculo de posse
    # FGA: Arremessos tentados, FTA: Lances livres, TOV: Turnovers, OREB: Rebotes Ofensivos
    relevant_stats = stats[['TEAM_NAME', 'TEAM_ID', 'FGA', 'FTA', 'TOV', 'OREB']]
    
    