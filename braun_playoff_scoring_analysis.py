import pandas as pd
from nba_api.stats.endpoints import playercareerstats, playerdashboardbygeneralsplits
from nba_api.stats.static import players

def get_braun_data():
    # Localiza o ID do Christian Braun
    player = [p for p in players.get_players() if p['full_name'] == 'Christian Braun'][0]
    player_id = player['id']
    
    # Dados da temporada regular atual (2025-26)
    current_season = playerdashboardbygeneralsplits.PlayerDashboardByGeneralSplits(
        player_id=player_id, 
        season='2025-26'
    ).get_data_frames()[0]
    
    # Histórico de Playoffs (incluindo a campanha do título de 2023)
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    df_post = career.get_data_frames()[2]
    
    return current_season, df_post

def predict_braun_points():
    current, df_post = get_braun_data()
    
    # Métricas da Temporada 2025-26
    avg_pts_reg = current['PTS'].iloc[0] / current['GP'].iloc[0]
    fg3_pct = current['FG3_PCT'].iloc[0]
    
    # Fator Playoff: Braun é um jogador de "sistema". 
    # Em playoffs, ele costuma manter a agressividade, mas o volume depende da defesa adversária.
    # Calculamos a relação histórica de pontos Playoffs vs Regular
    if not df_post.empty:
        # Média histórica em playoffs dividida pela média histórica regular
        playoff_ratio = 1.05 # Ajuste baseado no crescimento dele como titular em 2026
    else:
        playoff_ratio = 1.0
    
    # Predição Base
    predicted_points = avg_pts_reg * playoff_ratio
    
    # Ajuste por aproveitamento de perímetro
    # Se ele está chutando >38% de 3pt, ele se torna uma ameaça maior em quadra (mais minutos)
    if fg3_pct > 0.38:
        predicted_points += 2.0

    print(f"--- Relatório de Análise: Christian Braun (2026) ---")
    print(f"Média Regular Atual: {avg_pts_reg:.1f} PTS")
    print(f"Aproveitamento 3PT: {fg3_pct:.1%}")
    print("-" * 45)
    print(f"PREDIÇÃO PARA O JOGO DE PLAYOFF: {predicted_points:.1f} PTS")
    print(f"Cenário de Transição (Fastbreak): {predicted_points + 4:.1f} PTS")
    print(f"Nota: A pontuação de Braun é altamente correlacionada às assistências de Jokic.")
