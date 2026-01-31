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

   