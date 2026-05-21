import pandas as pd
from nba_api.stats.endpoints import playercareerstats

def predict_doncic_next_season():
    # ID fixo de Luka Dončić na NBA API
    doncic_id = 1629029
    
    print("Buscando historico de carreira de Luka Doncic...")
    career = playercareerstats.PlayerCareerStats(player_id=doncic_id)
    df_totals = career.get_data_frames()[0]
    
    # Filtrar apenas temporada regular
    df_reg = df_totals[df_totals['WHEN_MADE'] == 'Regular Season'].copy()
    
    if df_reg.empty:
        df_reg = df_totals
        
    # Calcular medias por jogo historicas
    df_reg['PPG'] = df_reg['PTS'] / df_reg['GP']
    df_reg['APG'] = df_reg['AST'] / df_reg['GP']
    df_reg['RPG'] = df_reg['REB'] / df_reg['GP']
    df_reg['MPG'] = df_reg['MIN'] / df_reg['GP']
    
    # Selecionar as ultimas 3 temporadas (teto de volume e maturidade)
    recent_seasons = df_reg.tail(3)
    
    if len(recent_seasons) < 3:
        print("Dados historicos insuficientes para calcular a tendencia.")
        return

    # Pesos para a media movel ponderada
    # Dando prioridade para o estilo de jogo e ritmo mais recente (50% para a ultima temporada)
    weights = [0.2, 0.3, 0.5]
    
    projected_pts = sum(recent_seasons['PPG'] * weights)
    projected_ast = sum(recent_seasons['APG'] * weights)
    projected_reb = sum(recent_seasons['RPG'] * weights)
    projected_min = sum(recent_seasons['MPG'] * weights)
    
    # --- Fator de Ajuste de Pico de Carreira (Peak Prime Factor) ---
    # Na fase dos 27-28 anos, armadores heliocentricos (onde o ataque orbita em torno de um jogador)
    # refinam a eficiencia de quadra (selecao de arremessos) sem perder volume de assistencias.
    peak_scoring_factor = 1.01   # Estabilizacao e refino de pontuacao (+1%)
    peak_passing_factor = 1.03   # Melhores leituras de dobra de defesa e passes no "pocket" (+3%)
    
    final_pts = projected_pts * peak_scoring_factor
    final_ast = projected_ast * peak_passing_factor
    final_reb = projected_reb * 1.00 # Manutencao do posicionamento de rebote defensivo
    
  