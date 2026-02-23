import pandas as pd
from nba_api.stats.endpoints import playergamelog
from sklearn.linear_model import LinearRegression
import numpy as np

# ID do Jusuf Nurkić (203994)
NURKIC_ID = '203994'

def predict_nurkic_performance():
    # 1. Buscar histórico de jogos da temporada 2025-26
    gamelog = playergamelog.PlayerGameLog(player_id=NURKIC_ID, season='2025-26')
    df = gamelog.get_data_frames()[0]
    
    # Inverter para ordem cronológica
    df = df.iloc[::-1].reset_index(drop=True)
    
    # 2. Engenharia de Variáveis (Features)
    # Vamos usar a média de pontos e rebotes dos últimos 5 jogos para prever o próximo
    df['PTS_LAST_5'] = df['PTS'].rolling(window=5).mean()
    df['REB_LAST_5'] = df['REB'].rolling(window=5).mean()
    df['AST_LAST_5'] = df['AST'].rolling(window=5).mean()
    
    # Remover linhas com valores nulos (os primeiros 5 jogos)
    df_model = df.dropna(subset=['PTS_LAST_5', 'REB_LAST_5', 'AST_LAST_5'])
    
    # 3. Treinar o Modelo (Prever Pontos)
    X = df_model[['PTS_LAST_5', 'REB_LAST_5', 'AST_LAST_5']]
    y = df_model['PTS']
    
    model = LinearRegression()
    model.fit(X, y)
    
    # 4. Predição para o próximo jogo
    # Usamos os dados mais recentes do dataframe
    latest_stats = X.iloc[[-1]]
    prediction = model.predict(latest_stats)
    
    print(f"--- Predição para Jusuf Nurkić ---")
    print(f"Média Recente (Últimos 5 jogos): {latest_stats['PTS_LAST_5'].values[0]:.1f} pts")
    print(f"Previsão de Pontos para o Próximo Jogo: {prediction[0]:.2f}")

if __name__ == "__main__":
    predict_nurkic_performance()
