import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats

def calcular_probabilidade_vitoria(rating_casa, rating_fora):
    diff = rating_fora - rating_casa
    return 1 / (10**(diff / 400) + 1)

def encontrar_winning_ticket_matchup(time_home, time_away):
    print(f"Buscando o 'Winning Ticket' para o confronto: {time_home} vs {time_away}...")

    # 1. Coleta da Rede Densa (Estatísticas 2025-26)
    # Pegamos estatísticas avançadas para identificar os "pesos" reais dos times
    stats = leaguedashteamstats.LeagueDashTeamStats(
        season='2025-26', measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    def extrair_rating_ticket(team_name):
        team_data = stats[stats['TEAM_NAME'] == team_name]
        if team_data.empty: return 1500 # Default Elo
        
        # 2. O Processo de Poda (Pruning)
        # Na LTH, removemos neurônios de baixa magnitude. 
        # Aqui, "podamos" o Net Rating bruto usando o PIE (Player Impact Estimate)
        # e o TS% (Eficiência) para isolar a sub-rede de vitórias consistentes.
        net_rating = team_data['NET_RATING'].values[0]
        pie = team_data['PIE'].values[0]
        ts_pct = team_data['TS_PCT'].values[0]

        # O Rating do Bilhete Premiado: 
        # Base 1500 + (Impacto Real * Eficiência) - descartando o ruído de vitórias "feias"
        ticket_rating = 1500 + (net_rating * 5) + (pie * 500) + (ts_pct * 100)
        return ticket_rating
