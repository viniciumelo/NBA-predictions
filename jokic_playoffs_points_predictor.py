import pandas as pd
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players

def get_jokic_stats():
    # Busca o ID do Nikola Jokic
    jokic = [p for p in players.get_players() if p['full_name'] == 'Nikola Jokic'][0]
    jokic_id = jokic['id']
    
    # Obtém estatísticas de carreira (Regular Season e Playoffs)
    career = playercareerstats.PlayerCareerStats(player_id=jokic_id)
    df_reg = career.get_data_frames()[0]  # Regular Season
    df_post = career.get_data_frames()[2] # Post Season (Playoffs)
    
    return df_reg, df_post

def predict_jokic_playoff_points():
    df_reg, df_post = get_jokic_stats()
    
    # Médias de Carreira - Temporada Regular
    reg_ppg = df_reg['PTS'].sum() / df_reg['GP'].sum()
    
    # Médias de Carreira - Playoffs
    playoff_ppg = df_post['PTS'].sum() / df_post['GP'].sum()
    
    # Fator de Elevação (Quanto ele aumenta a pontuação nos playoffs)
    elevation_factor = playoff_ppg / reg_ppg
    
    # Estatística da Temporada Atual (Última linha do DF de temporada regular)
    current_season_ppg = df_reg.iloc[-1]['PTS'] / df_reg.iloc[-1]['GP']
    
    # Predição para os Playoffs Baseada na Forma Atual
    predicted_points = current_season_ppg * elevation_factor
    
    print(f"--- Análise Nikola Jokic ---")
    print(f"Média Carreira (Regular): {reg_ppg:.1f} PTS")
    print(f"Média Carreira (Playoffs): {playoff_ppg:.1f} PTS")
    print(f"Fator de Elevação em Playoffs: {elevation_factor:.2%}")
    print("-" * 30)
    print(f"Média Temporada Atual: {current_season_ppg:.1f} PTS")
    print(f"PREDIÇÃO PARA OS PRÓXIMOS PLAYOFFS: {predicted_points:.1f} PTS")

if __name__ == "__main__":
    predict_jokic_playoff_points()