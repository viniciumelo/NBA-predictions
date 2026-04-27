import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def analisar_piores_reboteiros():
    # Coleta de dados da temporada 2025-26
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        per_mode_detailed='PerGame'
    ).get_data_frames()[0]
    
    # Filtro: Jogadores de alta minutagem (> 25 min/jogo)
    # Jogadores que jogam muito e pegam poucos rebotes são os "menos influentes" no vidro
    df = stats[stats['MIN'] > 25.0].copy()
    
    # Cálculo de Rebotes por Minuto (Métrica de eficiência)
    df['REB_PER_MIN'] = df['REB'] / df['MIN']
    
    # Ordenamos pelos menores valores
    piores = df.sort_values(by='REB_PER_MIN', ascending=True).head(10)
    
    print(f"=== ANÁLISE: JOGADORES COM MENOR EFICIÊNCIA DE REBOTE (MIN > 25) ===")
    print(piores[['PLAYER_NAME', 'MIN', 'REB', 'REB_PER_MIN']].to_string(index=False))
    
    print(f"\nNota: {piores.iloc[0]['PLAYER_NAME']} apresenta a menor taxa de rebotes por minuto")
    print("entre jogadores de rotação principal nesta temporada.")
