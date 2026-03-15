
import pandas as pd

# 1. Simulação de um Dataset (Estes dados seriam extraídos da nba_api ou CSV)
data = {
    'Time': ['Thunder', 'Pistons', 'Celtics', 'Spurs', 'Lakers', 'Nuggets'],
    'Vitorias': [52, 48, 43, 49, 42, 41],
    'Derrotas': [15, 18, 23, 18, 25, 27],
    'PPG': [118.6, 117.4, 114.2, 118.8, 116.5, 120.7],  # Pontos pró
    'OPPG': [107.8, 109.6, 107.0, 111.8, 115.3, 116.7]  # Pontos contra
}

df = pd.DataFrame(data)

# 2. Cálculo simples de Probabilidade (Margem de Vitória)
def prever_vencedor(time_a, time_b):
    try:
        stats_a = df[df['Time'] == time_a].iloc[0]
        stats_b = df[df['Time'] == time_b].iloc[0]
        
        # Calculamos o saldo médio de pontos (Net Rating simplificado)
        saldo_a = stats_a['PPG'] - stats_a['OPPG']
        saldo_b = stats_b['PPG'] - stats_b['OPPG']
        
        # Fator de força baseado na porcentagem de vitórias
        win_rate_a = stats_a['Vitorias'] / (stats_a['Vitorias'] + stats_a['Derrotas'])
        win_rate_b = stats_b['Vitorias'] / (stats_b['Vitorias'] + stats_b['Derrotas'])
        
        # Score de Predição (Peso 60% saldo de pontos, 40% histórico de vitórias)
        score_a = (saldo_a * 0.6) + (win_rate_a * 10)
        score_b = (saldo_b * 0.6) + (win_rate_b * 10)
        
        prob_a = (score_a / (score_a + score_b)) * 100 if (score_a + score_b) > 0 else 50

        print(f"--- Confronto: {time_a} vs {time_b} ---")
        if score_a > score_b:
            print(f"Vencedor provável: {time_a}")
            print(f"Chance estimada: {prob_a:.2f}%")
        else:
            print(f"Vencedor provável: {time_b}")
            print(f"Chance estimada: {100 - prob_a:.2f}%")
            
    except IndexError:
        print("Erro: Verifique se os nomes dos times estão corretos no banco de dados.")

