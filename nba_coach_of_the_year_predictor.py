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
    
    # Métrica: Win Percentage (O peso do sucesso absoluto)
    df['Win_Pct'] = (df['Wins'] / 82) * 100
    
    # Cálculo do COTY Score: (Surplus * 0.7) + (Win_Pct * 0.3)
    # O prêmio valoriza mais superar expectativas do que apenas ter o melhor recorde.
    df['COTY_Score'] = (df['Surplus_Wins'] * 0.7) + (df['Win_Pct'] * 0.3)
    
    # Ordenar pelos favoritos
    rank = df.sort_values(by='COTY_Score', ascending=False)
    
    