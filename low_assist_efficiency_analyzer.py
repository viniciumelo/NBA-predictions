import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def analisar_piores_passadores():
    # Coleta de dados
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        per_mode_detailed='PerGame'
    ).get_data_frames()[0]
    
    # Critério Acadêmico: 
    # Filtramos apenas jogadores com alta minutagem (> 25 min/jogo).
    # Jogadores que jogam muito mas distribuem pouco jogo têm o menor impacto de assistência.
    df = stats[stats['MIN'] > 25.0].copy()
    
    # Cálculo de Assistências por Minuto (Métrica de eficiência de distribuição)
    df['AST_PER_MIN'] = df['AST'] / df['MIN']
    
    # Ordenamos pelos menores valores
    piores = df.sort_values(by='AST_PER_MIN', ascending=True).head(10)
    
    print(f"=== ANÁLISE: JOGADORES COM MENOR EFICIÊNCIA DE PASSE (MIN > 25) ===")
    print(piores[['PLAYER_NAME', 'MIN', 'AST', 'AST_PER_MIN']].to_string(index=False))
    
    print(f"\nNota: Jogadores com menor AST_PER_MIN ocupam funções de finalização (Scoring)")
    print(f"e não de armação. {piores.iloc[0]['PLAYER_NAME']} é o menos eficiente nesta métrica.")

if __name__ == "__main__":
    analisar_piores_passadores()