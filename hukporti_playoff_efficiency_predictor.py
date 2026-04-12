import pandas as pd
from nba_api.stats.endpoints import playercareerstats, playerdashboardbygeneralsplits
from nba_api.stats.static import players

def get_hukporti_stats():
    # Localiza o ID do Ariel Hukporti
    player = [p for p in players.get_players() if p['full_name'] == 'Ariel Hukporti'][0]
    player_id = player['id']
    
    # Busca dados da temporada atual (2025-26)
    current_season = playerdashboardbygeneralsplits.PlayerDashboardByGeneralSplits(
        player_id=player_id, 
        season='2025-26'
    ).get_data_frames()[0]
    
    # Busca histórico de playoffs (se houver de 2025)
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    df_post = career.get_data_frames()[2]
    
    return current_season, df_post

def predict_points():
    current, df_post = get_hukporti_stats()
    
    # Estatísticas Base 2026
    gp = current['GP'].iloc[0]
    pts = current['PTS'].iloc[0]
    mins = current['MIN'].iloc[0]
    
    # Cálculo de Eficiência: Pontos por Minuto (PPM)
    ppm = pts / mins
    
    # Projeção de minutos em Playoffs (Cenário Realista: 3 a 5 minutos)
    playoff_minutes_low = 2.0
    playoff_minutes_high = 6.0
    
    # Predição
    pred_low = playoff_minutes_low * ppm
    pred_high = playoff_minutes_high * ppm
    
    print(f"--- Projeção de Playoffs 2026: Ariel Hukporti ---")
    print(f"Média Regular 25-26: {pts/gp:.1f} PTS em {mins/gp:.1f} MIN")
    print(f"Eficiência (PPM): {ppm:.3f}")
    print("-" * 45)
    print(f"Cenário de Rotação Curta: {pred_low:.1f} PTS")
    print(f"Cenário de Garbage Time: {pred_high:.1f} PTS")
    print(f"Teto (Caso jogue 12+ min): {12 * ppm:.1f} PTS")

if __name__ == "__main__":
    predict_points()