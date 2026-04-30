import pandas as pd

def predict_coach_of_the_year():
    # Dados baseados no encerramento da temporada regular 2025-26
    # 'Expected_Wins' é a projeção feita por analistas antes da temporada começar
    data = {
        'Treinador': ['Mark Daigneault', 'J.B. Bickerstaff', 'Gregg Popovich', 'Tom Thibodeau', 'Joe Mazzulla'],
        'Time': ['OKC Thunder', 'Detroit Pistons', 'SA Spurs', 'NY Knicks', 'Boston Celtics'],
        'Wins': [64, 60, 62, 53, 56],
        'Expected_Wins': [58, 35, 50, 52, 60]
    }
    
    df = pd.DataFrame(data)
    
    # Métrica: "Overachievement Score" (Quanto superou a expectativa)
    # Quanto maior a diferença entre vitórias reais e esperadas, maior a chance do prêmio.
    df['Surplus_Wins'] = df['Wins'] - df['Expected_Wins']
    
    