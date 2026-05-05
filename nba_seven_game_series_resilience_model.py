import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats

def predict_seven_game_winner():
    # Coleta dados avançados e de 'Clutch' da temporada 2025-26
    # O foco aqui é a capacidade de ajuste e sobrevivência em jogos parelhos
    stats = leaguedashteamstats.LeagueDashTeamStats(
        season='2025-26',
        measure_type_detailed_defense='Advanced'
    ).get_data_frames()[0]

    # Simulando dados de Clutch (votação/performance em momentos decisivos)
    # Em um cenário real, puxaríamos o endpoint 'LeagueDashPlayerClutch'
    # Aqui, focamos no Net Rating e na consistência (W_PCT)
    df = stats[['TEAM_NAME', 'W_PCT', 'NET_RATING', 'OFF_RATING', 'DEF_RATING']].copy()

    # Cálculo do Resilience Index (RI)
    # Séries longas premiam o equilíbrio. Multiplicamos Off e Def Rating.
    # Equipes equilibradas (bons nos dois lados) têm RI maior que especialistas.
    df['RESILIENCE_INDEX'] = (df['NET_RATING'] * 0.5) + (df['W_PCT'] * 50)
    
    