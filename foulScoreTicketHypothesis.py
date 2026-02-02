import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def encontrar_winning_ticket_faltas():
    print("Iniciando Poda Iterativa para isolar a sub-rede de 'Foul Trouble'...")
    
    # 1. A Rede Densa (Pool de parâmetros da temporada 2025-26)
    df = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        measure_type_detailed_advanced='Base'
    ).get_data_frames()[0]

    # 2. O Processo de Pruning (Poda)
    # Na LTH, removemos os neurônios de baixa magnitude. 
    # Cortamos quem não tem tempo de quadra suficiente para impactar a rede (MIN)
    # e quem tem um impacto defensivo insignificante (BLK/STL baixos), 
    # pois suas faltas costumam ser 'ruído' e não 'estratégia agressiva'.
    
    poda_minutos = df['MIN'].median()
    sub_rede = df[df['MIN'] >= poda_minutos].copy()

    