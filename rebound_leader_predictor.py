import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predict_rebound_leader():
    # Coleta estatísticas da temporada atual
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        per_mode_detailed='PerGame'
    ).get_data_frames()[0]
    
    # Filtramos jogadores que têm um volume alto de minutos para serem líderes
    # (Jogadores que jogam menos de 25min/jogo raramente lideram a liga)
    df = stats[stats['MIN'] > 25.0].copy()
    
    # Criamos o índice de rebote total projetado (Média * GP)
    df['TOTAL_REB_PROJ'] = df['REB'] * df['GP']
    
    # Ordenamos pelos melhores
    leader_rank = df.sort_values(by='REB', ascending=False).head(5)
    
    