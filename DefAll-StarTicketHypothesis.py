import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def encontrar_winning_ticket_defensivo():
    print("Aplicando Poda Iterativa para isolar o 'Bilhete Premiado' da defesa...")

    # 1. Coleta da Rede Densa (Dados de 2025-26)
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    # 2. O Processo de Poda (Pruning)
    # Na LTH, removemos os 'neurônios' (jogadores) que não atingem a magnitude mínima
    # Jogadores que jogam pouco ou têm impacto defensivo passivo são podados.
    media_def_rating = stats['DEF_RATING'].mean()
    poda_threshold = stats['MIN'].median()

    # Mantemos apenas quem joga minutos relevantes e está acima da média defensiva
    sub_rede = stats[
        (stats['MIN'] >= poda_threshold) & 
        (stats['DEF_RATING'] < media_def_rating) # Menor é melhor em DEF_RATING
    ].copy()

    