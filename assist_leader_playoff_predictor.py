import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats
from nba_api.stats.static import players

def get_playmaker_stats():
    # Coleta estatísticas de todos os jogadores ativos em 2025-26
    stats = leaguedashplayerstats.LeagueDashPlayerStats(season='2025-26').get_data_frames()[0]
    
    # Filtra jogadores com média alta de assistências (ex: > 7.0 AST/G)
    top_playmakers = stats[stats['AST'] > 7.0].sort_values(by='AST', ascending=False)
    
    return top_playmakers.head(10)

def predict_assist_leader():
    top_players = get_playmaker_stats()
    
   