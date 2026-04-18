import pandas as pd
from nba_api.stats.endpoints import playercareerstats, playerdashboardbygeneralsplits
from nba_api.stats.static import players

def get_ag_stats():
    # Localiza o ID do Aaron Gordon
    player = [p for p in players.get_players() if p['full_name'] == 'Aaron Gordon'][0]
    player_id = player['id']
    
    # Dados da temporada regular atual (2025-26)
    current_season = playerdashboardbygeneralsplits.PlayerDashboardByGeneralSplits(
        player_id=player_id, 
        season='2025-26'
    ).get_data_frames()[0]
    
    # Histórico de Playoffs (Essencial para analisar o "Playoff AG")
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    df_post = career.get_data_frames()[2]
    
    return current_season, df_post

def predict_gordon_points():
    try:
        current, hist = get_ag_stats()
        
        # Estatísticas Atuais (2025-26)
        avg_pts_reg = current['PTS'].iloc[0] / current['GP'].iloc[0]
        fg_pct = current['FG_PCT'].iloc[0]
        
        # Fator de Elevação em Playoffs
        # Gordon costuma manter ou subir a produção devido ao aumento de minutos
        if not hist.empty:
            # Pega as últimas 3 campanhas de playoffs para refletir o papel no Denver
            recent_post = hist.tail(3)
            post_avg = recent_post['PTS'].sum() / recent_post['GP'].sum()
            playoff_factor = post_avg / (hist['PTS'].sum() / hist['GP'].sum())
        else:
            playoff_factor = 1.08 # Ajuste padrão para aumento de minutagem
            
        # Predição Base
        # O modelo adiciona um bônus se a eficiência de quadra (FG%) for alta (>55%)
        # indicando que ele está ganhando as batalhas físicas no garrafão.
        efficiency_multiplier = 1.05 if fg_pct > 0.55 else 1.0
        predicted_points = (avg_pts_reg * playoff_factor) * efficiency_multiplier

        print(f"=== ANALISE DE PREDICAO: AARON GORDON (2026) ===")
        print(f"Media Regular Atual: {avg_pts_reg:.1f} PTS")
        print(f"Eficiencia (FG%): {fg_pct:.1%}")
        print("-" * 45)
        print(f"PREDICAO PARA JOGO DE PLAYOFF: {predicted_points:.1f} PTS")
        print(f"Teto (Mismatch Ofensivo): {predicted_points + 5:.1f} PTS")
        print(f"Piso (Foco Defensivo): {predicted_points - 3.0:.1f} PTS")
        print(f"\nNota: A pontuacao de Gordon depende 70% de pontos na tinta (dunks/layups).")

    except Exception as e:
        print(f"Erro ao processar dados: {e}")
