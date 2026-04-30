import pandas as pd

def predict_best_playoff_coach():
    # Simulando dados consolidados dos Playoffs 2026
    # Ajustes: Quantidade de vezes que o técnico mudou a rotação e venceu o jogo seguinte
    # Road_Wins: Vitórias fora de casa (prova de preparação mental/tática)
    data = {
        'Treinador': ['Mark Daigneault', 'Gregg Popovich', 'J.B. Bickerstaff', 'Erik Spoelstra'],
        'Time': ['OKC Thunder', 'SA Spurs', 'Detroit Pistons', 'Miami Heat'],
        'Series_Vencidas': [3, 2, 1, 1],
        'Road_Wins': [5, 4, 2, 3],
        'Tactical_Adjustments': [8, 10, 4, 9],
        'Win_Percentage': [0.750, 0.640, 0.500, 0.550]
    }
    
    df = pd.DataFrame(data)
    
    # Cálculo do Playoff Impact Score (PIS)
    # Peso 40% para vitórias fora de casa, 40% para ajustes táticos e 20% para % de vitórias
    df['Playoff_Impact_Score'] = (
        (df['Road_Wins'] * 4.0) + 
        (df['Tactical_Adjustments'] * 4.0) + 
        (df['Win_Percentage'] * 100 * 0.2)
    )
    
    