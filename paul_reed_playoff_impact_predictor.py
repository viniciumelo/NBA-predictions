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

        # --- Definição de Cenários Estocásticos ---
        # Em Python, usamos dicionários para mapear variáveis de ambiente (minutos)
        cenarios_minutos = {
            "Rotação Curta (Padrao)": 10.0,
            "Problemas de Faltas do Titular": 18.0,
            "Cenário de Alta minutagem": 25.0
        }

        print(f"=== ANALISE DE PREDICAO: PAUL REED (2026) ===")
        print(f"Eficiencia Atual (PPM): {ppm_regular:.3f}")
        print(f"Eficiencia Projetada Playoff (PPM): {ppm_playoff:.3f}")
        print("-" * 45)

        # Iteração sobre cenários para gerar o range de predição
        for cenario, minutos in cenarios_minutos.items():
            predicao = minutos * ppm_playoff
            print(f"{cenario:.<35}: {predicao:>5.1f} PTS")

    except Exception as e:
        print(f"Erro na análise de dados: {e}")
