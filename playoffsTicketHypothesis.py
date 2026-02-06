import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats

def predicao_playoffs_lottery_ticket(time_a, time_b):
    print(f"Buscando o 'Winning Ticket' para o confronto: {time_a} vs {time_b}...")

    # 1. Coleta da Rede Densa (Estatísticas de Temporada e Playoffs 2025-26)
    # Na LTH, começamos com a rede completa para identificar os pesos iniciais
    stats = leaguedashteamstats.LeagueDashTeamStats(
        season='2025-26',
        measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    def extrair_bilhete_vencedor(team_name):
        team_data = stats[stats['TEAM_NAME'] == team_name]
        if team_data.empty: return None
        
        # 2. O Processo de Poda (Pruning)
        # Em Playoffs, 'podamos' o ruído. Times que dependem de banco (bench) 
        # ou volume sem eficiência perdem magnitude. 
        # O 'Winning Ticket' é a combinação de Net Rating + Eficiência Real (TS%)
        net_rating = team_data['NET_RATING'].values[0]
        ts_pct = team_data['TS_PCT'].values[0]
        pie = team_data['PIE'].values[0] # Player Impact Estimate (Impacto da sub-rede)
        
        # O Score do Bilhete: Peso maior para PIE e TS% (métrica de 'clutch')
        ticket_score = (net_rating * 0.5) + (ts_pct * 100 * 0.3) + (pie * 100 * 0.2)
        return ticket_score, net_rating

   