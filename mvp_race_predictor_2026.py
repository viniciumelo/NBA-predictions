import pandas as pd

def calcular_score_mvp():
    # Dados simulados baseados na performance da temporada 2025-26 até agora
    # Métricas: [PTS, PER, Win_Shares, Team_Wins]
    # Pesos (importância relativa para o voto do MVP)
    # Win_Shares: 30%, Team_Wins: 30%, PER: 25%, PTS: 15%
    
    data = {
        'Jogador': ['Wembanyama', 'Jokic', 'SGA'],
        'PTS': [25.5, 26.2, 30.5],
        'PER': [28.5, 31.0, 29.5],
        'Win_Shares': [12.0, 14.5, 13.0],
        'Team_Wins': [52, 58, 55]
    }
    
    df = pd.DataFrame(data)
    
    # Normalização simples (0 a 1) para comparar métricas com escalas diferentes
    for col in ['PTS', 'PER', 'Win_Shares', 'Team_Wins']:
        df[f'{col}_norm'] = df[col] / df[col].max()
    
    # Cálculo do Score Final com Pesos
    df['MVP_Score'] = (
        (df['Win_Shares_norm'] * 0.30) +
        (df['Team_Wins_norm'] * 0.30) +
        (df['PER_norm'] * 0.25) +
        (df['PTS_norm'] * 0.15)
    ) * 100
    
    # Ordenar por maior pontuação
    df = df.sort_values(by='MVP_Score', ascending=False)
    
    print(f"=== ANÁLISE DE PREDICAÇÃO: MVP NBA 2026 ===")
    for index, row in df.iterrows():
        print(f"{row['Jogador']}: {row['MVP_Score']:.2f} pontos de probabilidade")
    