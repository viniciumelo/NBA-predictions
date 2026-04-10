import pandas as pd
from nba_api.stats.endpoints import playercareerstats, playerdashboardbygeneralsplits
from nba_api.stats.static import players

def get_ant_data():
    # Localiza o ID do Anthony Edwards
    ant = [p for p in players.get_players() if p['full_name'] == 'Anthony Edwards'][0]
    ant_id = ant['id']
    
    # Busca histórico de carreira (Regular vs Playoffs)
    career = playercareerstats.PlayerCareerStats(player_id=ant_id)
    df_reg_career = career.get_data_frames()[0]
    df_post_career = career.get_data_frames()[2]
    
    # Busca dados da temporada atual (2025-26)
    current_season = playerdashboardbygeneralsplits.PlayerDashboardByGeneralSplits(
        player_id=ant_id,
        season='2025-26'
    ).get_data_frames()[0]
    
    return df_reg_career, df_post_career, current_season

def predict_ant_man_points():
    df_reg, df_post, current = get_ant_data()
    
    # Médias de Carreira
    career_reg_avg = df_reg['PTS'].sum() / df_reg['GP'].sum()
    career_post_avg = df_post['PTS'].sum() / df_post['GP'].sum()
    
    # O "Ant-Man Peak": Proporção de crescimento histórico em playoffs
    # Edwards costuma subir cerca de 15-20% sua pontuação
    playoff_multiplier = career_post_avg / career_reg_avg
    
    # Dados da temporada atual 2025-26
    current_ppg = current['PTS'].iloc[0] / current['GP'].iloc[0]
    
    # Predição: Média atual ajustada pelo fator de crescimento em playoffs
    # Adicionamos um ajuste de +5% para o amadurecimento físico dele em 2026
    predicted_points = (current_ppg * playoff_multiplier) * 1.05

    print(f"--- Predição Estatística: Anthony Edwards (Ant-Man) ---")
    print(f"Média Temporada Atual: {current_ppg:.1f} PTS")
    print(f"Histórico de Elevação em Playoffs: {playoff_multiplier:.2%}")
    print("-" * 50)
    print(f"PREDIÇÃO PARA O JOGO DE PLAYOFF: {predicted_points:.1f} PTS")
    print(f"Teto de Explosão (Modo Elite): {predicted_points + 7:.1f} PTS")
    print(f"Piso de Performance: {predicted_points - 4.5:.1f} PTS")

if __name__ == "__main__":
    predict_ant_man_points()