import pandas as pd
from nba_api.stats.endpoints import playercareerstats, playerdashboardbygeneralsplits
from nba_api.stats.static import players

def get_booker_stats():
    # Localiza o ID do Devin Booker
    player = [p for p in players.get_players() if p['full_name'] == 'Devin Booker'][0]
    player_id = player['id']
    
    # Dados da temporada atual (2025-26)
    current_season = playerdashboardbygeneralsplits.PlayerDashboardByGeneralSplits(
        player_id=player_id, 
        season='2025-26'
    ).get_data_frames()[0]
    
    # Histórico de Playoffs
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    df_post = career.get_data_frames()[2]
    
    return current_season, df_post

def predict_booker_points():
    try:
        current, hist = get_booker_stats()
        
        # Métricas da Temporada 2025-26
        avg_pts_reg = current['PTS'].iloc[0] / current['GP'].iloc[0]
        avg_min_reg = current['MIN'].iloc[0] / current['GP'].iloc[0]
        
        # Fator de Playoff: Booker costuma aumentar o volume (FGA) nos playoffs
        if not hist.empty:
            recent_post = hist.tail(3) # Foca nas últimas 3 temporadas
            post_avg = recent_post['PTS'].sum() / recent_post['GP'].sum()
            playoff_factor = post_avg / (hist['PTS'].sum() / hist['GP'].sum())
        else:
            playoff_factor = 1.05 # Estimativa de aumento de volume
            
        # O modelo aplica uma projeção de minutos: Estrelas como Booker
        # tendem a jogar cerca de 38-40 minutos em jogos de playoff.
        projected_min = 39.0
        points_per_minute = avg_pts_reg / avg_min_reg
        
        predicted_points = (points_per_minute * projected_min) * playoff_factor

        print(f"=== ANALISE DE PREDICAO: DEVIN BOOKER (2026) ===")
        print(f"Media Regular Atual: {avg_pts_reg:.1f} PTS")
        print(f"Media de Minutos (Regular): {avg_min_reg:.1f}")
        print("-" * 45)
        print(f"PROJECAO PARA JOGO DE PLAYOFF (40 min): {predicted_points:.1f} PTS")
        print(f"Teto (Modo 'Suns System'): {predicted_points + 8:.1f} PTS")
        print(f"Piso (Defesa Ajustada): {predicted_points - 5:.1f} PTS")
        print(f"\nNota: Booker e um dos jogadores que mais tem variacao baseada em 'Shot Quality'.")

    except Exception as e:
        print(f"Erro ao processar dados: {e}")

if __name__ == "__main__":
    predict_booker_points()