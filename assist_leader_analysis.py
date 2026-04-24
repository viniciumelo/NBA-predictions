import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predict_assist_leader_2026():
    # Coleta estatísticas da temporada 2025-26
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        per_mode_detailed='PerGame'
    ).get_data_frames()[0]
    
    # Filtra apenas jogadores com alta carga de assistências (> 6.0 AST/G)
    # e que possuem pelo menos 50 jogos (para garantir consistência estatística)
    df = stats[(stats['AST'] > 6.0) & (stats['GP'] > 50)].copy()
    
    