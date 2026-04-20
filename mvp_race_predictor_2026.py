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
    