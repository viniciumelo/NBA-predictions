import pandas as pd
from nba_api.stats.endpoints import playercareerstats, playerdashboardbygeneralsplits
from nba_api.stats.static import players

def get_lebron_data():
    # Localiza o ID do LeBron James
    lbj = [p for p in players.get_players() if p['full_name'] == 'LeBron James'][0]
    lbj_id = lbj['id']
    
    # Busca histórico de carreira (Regular vs Playoffs)
    career = playercareerstats.PlayerCareerStats(player_id=lbj_id)
    df_reg_career = career.get_data_frames()[0]
    df_post_career = career.get_data_frames()[2]
    
    # Busca dados da temporada atual (2025-26)
    current_season = playerdashboardbygeneralsplits.PlayerDashboardByGeneralSplits(
        player_id=lbj_id,
        season='2025-26'
    ).get_data_frames()[0]
    
    return df_reg_career, df_post_career, current_season

def predict_lebron_points():
    df_reg, df_post, current = get_lebron_data()
    
    # Médias de Carreira
    career_reg_avg = df_reg['PTS'].sum() / df_reg['GP'].sum()
    career_post_avg = df_post['PTS'].sum() / df_post['GP'].sum()
    
    # O "Playoff Mode": Proporção de aumento histórico do LeBron
    playoff_multiplier = career_post_avg / career_reg_avg
    
    # Dados da temporada 2025-26
    current_ppg = current['PTS'].iloc[0] / current['GP'].iloc[0]
    current_min = current['MIN'].iloc[0] / current['GP'].iloc[0]
    
    # Predição Base: Média atual x multiplicador de playoff
    # Ajuste adicional: LeBron costuma jogar +15% de minutos nos playoffs aos 41 anos
    min_adjustment = 1.15 
    predicted_points = (current_ppg * playoff_multiplier) * (1 + (min_adjustment - 1) * 0.5)

    print(f"--- Análise Estatística: LeBron James (Season 23) ---")
    print(f"Média Atual (2025-26): {current_ppg:.1f} PTS")
    print(f"Multiplicador Histórico de Playoffs: {playoff_multiplier:.2%}")
    print("-" * 45)
    print(f"PREDIÇÃO PARA O PRÓXIMO JOGO DE PLAYOFF: {predicted_points:.1f} PTS")
    print(f"Teto Estimado (Jogos de Eliminação): {predicted_points + 6:.1f} PTS")

if __name__ == "__main__":
    predict_lebron_points()