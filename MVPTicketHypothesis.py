import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predicao_mvp_lottery_ticket():
    print("Iniciando Poda Iterativa para isolar o 'Winning Ticket' do MVP 2026...")
    
    # 1. Coleta da Rede Densa (Todos os jogadores)
    # Usamos Advanced Stats para capturar a 'arquitetura' real do impacto
    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26', 
        measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    # 2. O Processo de Poda (Pruning)
    # Removemos neurônios (jogadores) com baixa magnitude de impacto
    # Um 'Winning Ticket' precisa de volume (USG_PCT) e eficiência (NET_RATING)
    threshold_min = 32
    threshold_usg = player_stats['USG_PCT'].median()
    
    # Poda: Mantemos apenas a sub-rede de alto uso e alta minutagem
    sub_rede = player_stats[
        (player_stats['MIN'] >= threshold_min) & 
        (player_stats['USG_PCT'] >= threshold_usg)
    ].copy()

   