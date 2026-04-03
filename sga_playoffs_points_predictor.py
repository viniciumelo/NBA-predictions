import pandas as pd
from nba_api.stats.endpoints import playercareerstats, playerdashboardbygeneralsplits
from nba_api.stats.static import players
import time

def get_sga_prediction_data():
    # Busca o ID do Shai
    sga = [p for p in players.get_players() if p['full_name'] == 'Shai Gilgeous-Alexander'][0]
    sga_id = sga['id']
    
# 1. Estatísticas de Carreira (Histórico Regular vs Playoffs)
    career = playercareerstats.PlayerCareerStats(player_id=sga_id)
    df_reg_career = career.get_data_frames()[0]
    df_post_career = career.get_data_frames()[2]
    
    # 2. Forma Atual (Temporada 2025-26)
    current_season = playerdashboardbygeneralsplits.PlayerDashboardByGeneralSplits(
        player_id=sga_id, 
        season='2025-26'
    ).get_data_frames()[0]
    
    return df_reg_career, df_post_career, current_season

def predict_sga_points():
    df_reg, df_post, current = get_sga_prediction_data()
    
    # Médias Históricas
    reg_ppg = df_reg['PTS'].sum() / df_reg['GP'].sum()
    playoff_ppg = df_post['PTS'].sum() / df_post['GP'].sum()
    
    # Fator de Ajuste: Como o rendimento dele muda em Playoffs
    # Shai é um jogador de "ritmo controlado", a variação costuma ser pequena
    adjustment_factor = playoff_ppg / reg_ppg
    
    # Dados Atuais (2025-26)
    current_ppg = current['PTS'].iloc[0] / current['GP'].iloc[0]
    current_ft_rate = current['FTA'].iloc[0] / current['FGA'].iloc[0]
    
    # Predição: Média Atual ajustada pelo histórico + bônus de agressividade (lances livres)
    # Em playoffs, o volume de lances livres do SGA tende a subir
    predicted_points = (current_ppg * adjustment_factor) + (current_ft_rate * 2)
    
    print(f"--- Relatório de Predição: SGA 2026 ---")
    print(f"Média Atual (2025-26): {current_ppg:.1f} PTS")
    print(f"Aproveitamento FT Atual: {current.iloc[0]['FT_PCT']:.1%}")
    print("-" * 35)
    print(f"PREDIÇÃO PARA JOGO DE PLAYOFF: {predicted_points:.1f} PTS")
    print(f"Intervalo Estimado: {predicted_points-3:.1f} - {predicted_points+5:.1f}")

if __name__ == "__main__":
    predict_sga_points()
