import pandas as pd
from nba_api.stats.endpoints import playercareerstats, playerdashboardbygeneralsplits
from nba_api.stats.static import players

def obter_dados_analise():
    # Localiza o ID via string matching
    player = [p for p in players.get_players() if p['full_name'] == 'Paul Reed'][0]
    player_id = player['id']
    
    # Coleta de dados da temporada regular atual (2025-26)
    # O endpoint dashboard fornece divisões granulares de estatísticas
    current_season = playerdashboardbygeneralsplits.PlayerDashboardByGeneralSplits(
        player_id=player_id, 
        season='2025-26'
    ).get_data_frames()[0]
    
    # Coleta de dados históricos de Playoffs para comparação de intensidade
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    df_playoffs_hist = career.get_data_frames()[2]
    
    return current_season, df_playoffs_hist

def prever_pontos_por_cenario():
    try:
        current, hist = obter_dados_analise()
        
        # --- Cálculo de Métricas de Eficiência ---
        # PPM (Points Per Minute) é a métrica chave para jogadores de rotação
        pts_atual = current['PTS'].iloc[0]
        min_atual = current['MIN'].iloc[0]
        ppm_regular = pts_atual / min_atual
        
        # Determinação do PPM de Playoff (Fator de Intensidade)
        if not hist.empty:
            # Se houver histórico, calculamos a eficiência real de pós-temporada
            ppm_playoff = hist['PTS'].sum() / hist['MIN'].sum()
        else:
            # Caso contrário, aplica-se um acréscimo de 5% (ajuste de esforço defensivo/rebote)
            ppm_playoff = ppm_regular * 1.05

        