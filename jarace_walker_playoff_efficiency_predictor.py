import pandas as pd
from nba_api.stats.endpoints import playerdashboardbygeneralsplits
from nba_api.stats.static import players

def get_walker_data():
    # Localiza o ID do Jarace Walker
    player = [p for p in players.get_players() if p['full_name'] == 'Jarace Walker'][0]
    player_id = player['id']
    
    # Dados da temporada atual (2025-26)
    current_season = playerdashboardbygeneralsplits.PlayerDashboardByGeneralSplits(
        player_id=player_id, 
        season='2025-26'
    ).get_data_frames()[0]
    
    return current_season

def predict_walker_points():
    current = get_walker_data()
    
    # Métricas Base (Temporada 2025-26)
    pts_avg = current['PTS'].iloc[0] / current['GP'].iloc[0]
    min_avg = current['MIN'].iloc[0] / current['GP'].iloc[0]
    
    # Métrica de Performance: Pontos por Minuto (PPM)
    ppm = pts_avg / min_avg
    
    # Fator de Playoff:
    # Em séries de playoffs, o ritmo (Pace) tende a cair um pouco, 
    # mas a intensidade defensiva aumenta. Projetamos uma manutenção da eficiência (1.0).
    playoff_intensity_factor = 1.0
    
    # Cenários de Rotação (A minutagem em playoffs é volátil)
    cenarios = {
        "Rotação Rotineira (12 min)": 12.0,
        "Cenário de Alta Rotação (18 min)": 18.0
    }
    
    print(f"=== ANALISE DE PREDICAO: JARACE WALKER (2026) ===")
    print(f"Média Regular: {pts_avg:.1f} PTS | Minutos: {min_avg:.1f}")
    print(f"Eficiência (PPM): {ppm:.3f}")
    print("-" * 50)
    
   