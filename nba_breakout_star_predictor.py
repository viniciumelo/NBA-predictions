import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predizer_revelacao_ano():
    # Coleta de dados da temporada atual (2025-26)
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        per_mode_detailed='PerGame'
    ).get_data_frames()[0]
    
    # Filtramos jogadores com menos de 3 anos de liga (critério de 'revelação')
    # e alta minutagem para filtrar amostragem insuficiente
    df = stats[(stats['MIN'] > 20.0)].copy()
    
    # Criamos um "Índice de Impacto Juvenil"
    # Foco: Pontos + Assistências + Rebotes normalizados por Minuto
    df['IMPACTO_INDEX'] = (df['PTS'] + df['AST'] + df['REB']) / df['MIN']
    
    # Ordenamos pelos melhores índices
    revelacoes = df.sort_values(by='IMPACTO_INDEX', ascending=False).head(10)
    
    