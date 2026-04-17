import pandas as pd
from nba_api.stats.endpoints import playercareerstats, playerdashboardbygeneralsplits
from nba_api.stats.static import players

def get_zubac_data():
    # Localiza o ID do Ivica Zubac
    player = [p for p in players.get_players() if p['full_name'] == 'Ivica Zubac'][0]
    player_id = player['id']
    
    # Dados da temporada regular atual (2025-26)
    current_season = playerdashboardbygeneralsplits.PlayerDashboardByGeneralSplits(
        player_id=player_id, 
        season='2025-26'
    ).get_data_frames()[0]
    
    # Histórico de Playoffs (Zubac tem vasta experiência em pós-temporada)
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    df_post = career.get_data_frames()[2]
    
    return current_season, df_post

def predict_zubac_points():
    current, df_post = get_zubac_data()
    
    # Métricas da Temporada 2025-26
    avg_pts_reg = current['PTS'].iloc[0] / current['GP'].iloc[0]
    ft_pct = current['FT_PCT'].iloc[0]
    fg_pct = current['FG_PCT'].iloc[0]
    
    # Fator Playoff: Zubac é um jogador de "piso alto"
    # Nos playoffs, ele costuma jogar minutos mais físicos contra pivôs de elite
    if not df_post.empty:
        # Calculamos a relação histórica: Pontos Playoff / Pontos Regular
        playoff_history_ratio = (df_post['PTS'].sum() / df_post['GP'].sum()) / (avg_pts_reg)
    else:
        playoff_history_ratio = 0.95 # Pequeno ajuste conservador se não houver dados
    
    # Ajuste de Eficiência (Regra de Negócio)
    # Zubac acima de 60% de FG indica que ele está dominando o garrafão
    efficiency_bonus = 1.10 if fg_pct > 0.60 else 1.0
    
    # Predição Final
    predicted_points = (avg_pts_reg * playoff_history_ratio) * efficiency_bonus

    print(f"--- Relatório de Análise: Ivica Zubac (2026) ---")
    print(f"Média Regular Atual: {avg_pts_reg:.1f} PTS")
    print(f"Aproveitamento de Quadra (FG%): {fg_pct:.1%}")
    print("-" * 45)
    print(f"PREDIÇÃO PARA O JOGO DE PLAYOFF: {predicted_points:.1f} PTS")
    print(f"Piso (Double-Double Thread): {predicted_points - 3:.0f} PTS")
    print(f"Teto (Aproveitamento em Faltas): {predicted_points + 4:.1f} PTS")
    print(f"Nota: A pontuação de Zubac depende 90% de pontos na tinta e lances livres.")

if __name__ == "__main__":
    predict_zubac_points()