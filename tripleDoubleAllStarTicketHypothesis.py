import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def encontrar_winning_ticket_triple_double():
    print("Iniciando Poda Iterativa para isolar a sub-rede de versatilidade (Triple-Double)...")
    
    # 1. Coleta da Rede Densa (Dados de 2025-26)
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    # 2. O Processo de Poda (Pruning)
    # Na LTH, removemos neurônios que não contribuem para a tarefa específica.
    # Filtramos jogadores com USG% alto (protagonistas) e PIE acima da média.
    threshold_pie = stats['PIE'].mean()
    
    # Poda: Mantemos apenas a sub-rede que impacta o jogo globalmente
    sub_rede = stats[
        (stats['PIE'] > threshold_pie) & 
        (stats['AST_PCT'] > 0.15) & # Deve ser responsável por pelo menos 15% das assistências
        (stats['REB_PCT'] > 0.08)   # Deve capturar pelo menos 8% dos rebotes disponíveis
    ].copy()
