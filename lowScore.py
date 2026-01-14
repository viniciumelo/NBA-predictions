import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predicao_menos_pontos():
    print("Analisando jogadores de baixa produção ofensiva...")
    
    # 1. Coletar dados da temporada atual
    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    # 2. Filtro de "Titulares ou Rotação" 
    # Buscamos jogadores que jogam muito (25+ min) mas pontuam pouco
    titulares_pouco_uso = player_stats[player_stats['MIN'] >= 25].copy()

    # 3. Cálculo do "Low Score Risk"
    # Valorizamos: Baixo Usage Rate + Baixa Média de Pontos
    # O USG% baixo indica que o time não desenha jogadas para ele.
    titulares_pouco_uso['LOW_SCORE_RISK'] = (
        (1 / titulares_pouco_uso['USG_PCT']) * 10 + 
        (1 / titulares_pouco_uso['PTS']) * 100
    )

   