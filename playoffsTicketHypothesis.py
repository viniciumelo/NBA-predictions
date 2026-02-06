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

    score_a, net_a = extrair_bilhete_vencedor(time_a)
    score_b, net_b = extrair_bilhete_vencedor(time_b)

    if score_a is None or score_b is None:
        return "Erro: Dados insuficientes para identificar os bilhetes."

    # 3. Comparação de Sub-redes (Predição)
    # A diferença entre os Winning Tickets indica quem tem a estrutura mais resiliente
    diff_ticket = score_a - score_b
    prob_a = 50 + (diff_ticket * 2.0)
    prob_a = max(min(prob_a, 98), 2) # Playoffs são mais extremos (2% a 98%)

    print(f"\n--- ANÁLISE DO WINNING TICKET (Playoffs 2026) ---")
    print(f"{time_a}: Ticket Score {score_a:.2f} (Net: {net_a})")
    print(f"{time_b}: Ticket Score {score_b:.2f} (Net: {net_b})")
    print("-" * 30)
    print(f"PREDIÇÃO FINAL: {time_a} tem {prob_a:.1f}% de chance de vencer a série.")
    
    return prob_a

# Exemplo de uso
predicao_playoffs_lottery_ticket("Boston Celtics", "Dallas Mavericks")