import pandas as pd
from nba_api.stats.endpoints import playercareerstats

def predict_wemby_next_season():
    # ID fixo de Victor Wembanyama na NBA API
    wemby_id = 1641705
    
    print("Buscando histórico de carreira de Victor Wembanyama...")
    career = playercareerstats.PlayerCareerStats(player_id=wemby_id)
    df_totals = career.get_data_frames()[0]
    
    # Filtrar apenas temporada regular
    df_reg = df_totals[df_totals['WHEN_MADE'] == 'Regular Season'].copy()
    
    if df_reg.empty:
        df_reg = df_totals
        
    # Calcular médias por jogo históricas
    df_reg['PPG'] = df_reg['PTS'] / df_reg['GP']
    df_reg['APG'] = df_reg['AST'] / df_reg['GP']
    df_reg['RPG'] = df_reg['REB'] / df_reg['GP']
    df_reg['BPG'] = df_reg['BLK'] / df_reg['GP']
    df_reg['MPG'] = df_reg['MIN'] / df_reg['GP']
    
    # Analisar o histórico recente de evolução
    recent_seasons = df_reg.tail(3)
    
    # Definir pesos baseados na quantidade de dados disponíveis
    # Como ele tem poucas temporadas, damos o maior peso para o ano mais recente
    if len(recent_seasons) >= 2:
        weights = [0.3, 0.7] if len(recent_seasons) == 2 else [0.1, 0.3, 0.6]
        projected_pts = sum(recent_seasons['PPG'].tail(len(weights)) * weights)
        projected_ast = sum(recent_seasons['APG'].tail(len(weights)) * weights)
        projected_reb = sum(recent_seasons['RPG'].tail(len(weights)) * weights)
        projected_blk = sum(recent_seasons['BPG'].tail(len(weights)) * weights)
        projected_min = sum(recent_seasons['MPG'].tail(len(weights)) * weights)
    else:
        # Fallback caso só haja uma temporada registrada
        projected_pts = recent_seasons['PPG'].iloc[0]
        projected_ast = recent_seasons['APG'].iloc[0]
        projected_reb = recent_seasons['RPG'].iloc[0]
        projected_blk = recent_seasons['BPG'].iloc[0]
        projected_min = recent_seasons['MPG'].iloc[0]

    # --- Fator de Desenvolvimento de Unicórnio (Anos 4 e 5) ---
    # Jogadores com o perfil físico e técnico do Wemby tendem a dar um salto de eficiência 
    # à medida que o time adiciona armadores de elite.
    growth_factor_scoring = 1.06  # +6% de evolução em pontos devido a melhor seleção de arremessos
    growth_factor_defense = 1.02  # +2% em rebotes/tocos (estabilização por dominância natural)
    
    final_pts = projected_pts * growth_factor_scoring
    final_ast = projected_ast * growth_factor_scoring
    final_reb = projected_reb * growth_factor_defense
    final_blk = projected_blk * growth_factor_defense
    
    