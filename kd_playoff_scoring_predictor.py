import pandas as pd
from nba_api.stats.endpoints import playercareerstats, playerdashboardbygeneralsplits
from nba_api.stats.static import players

def get_kd_stats():
    # Localiza o ID do Kevin Durant
    kd = [p for p in players.get_players() if p['full_name'] == 'Kevin Durant'][0]
    kd_id = kd['id']
    
    # Busca estatísticas de carreira (Regular vs Playoffs)
    career = playercareerstats.PlayerCareerStats(player_id=kd_id)
    df_reg_career = career.get_data_frames()[0]
    df_post_career = career.get_data_frames()[2]
    
    # Busca dados da temporada atual (2025-26)
    current_season = playerdashboardbygeneralsplits.PlayerDashboardByGeneralSplits(
        player_id=kd_id,
        season='2025-26'
    ).get_data_frames()[0]
    
    return df_reg_career, df_post_career, current_season

def predict_kd_points():
    df_reg, df_post, current = get_kd_stats()
    
    # Médias de Carreira
    reg_avg = df_reg['PTS'].sum() / df_reg['GP'].sum()
    post_avg = df_post['PTS'].sum() / df_post['GP'].sum()
    
    # Fator KD: O quanto ele mantém ou aumenta a produção sob pressão
    # Durant é conhecido por manter a eficiência mesmo contra defesas de playoff
    playoff_consistency_factor = post_avg / reg_avg
    
    # Dados 2025-26
    current_ppg = current['PTS'].iloc[0] / current['GP'].iloc[0]
    current_fg_pct = current['FG_PCT'].iloc[0]
    
    # Predição: Média atual ajustada pela consistência histórica
    # Adicionamos um pequeno ajuste de "Volume de Estrela" (+5% de arremessos)
    predicted_points = (current_ppg * playoff_consistency_factor) * 1.05
    
    print(f"--- Relatório de Predição: Kevin Durant ---")
    print(f"Média Temporada Regular (Carreira): {reg_avg:.1f} PTS")
    print(f"Média Playoffs (Carreira): {post_avg:.1f} PTS")
    print("-" * 40)
    print(f"Média Atual (2025-26): {current_ppg:.1f} PTS")
    print(f"Aproveitamento FG Atual: {current_fg_pct:.1%}")
    print(f"PREDIÇÃO PARA O PRÓXIMO JOGO DE PLAYOFF: {predicted_points:.1f} PTS")
    print(f"Zona de Conforto: {predicted_points-2:.0f} a {predicted_points+4:.0f} PTS")

if __name__ == "__main__":
    predict_kd_points()