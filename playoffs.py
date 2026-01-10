import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats

def predicao_playoffs(time_a, time_b):
    # 1. Coletar estatísticas de equipes focadas em 'Playoffs'
    # O parâmetro MeasureType='Advanced' traz o NetRating (métrica de ouro)
    stats = leaguedashteamstats.LeagueDashTeamStats(
        season='2023-24', 
        season_type_all_star='Playoffs',
        measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    def get_team_metrics(team_name):
        team_data = stats[stats['TEAM_NAME'] == team_name]
        if team_data.empty: return None
        return {
            'net_rating': team_data['NET_RATING'].values[0],
            'off_rating': team_data['OFF_RATING'].values[0],
            'def_rating': team_data['DEF_RATING'].values[0],
            'true_shooting': team_data['TS_PCT'].values[0]
        }

    metrics_a = get_team_metrics(time_a)
    metrics_b = get_team_metrics(time_b)

    if not metrics_a or not metrics_b:
        return "Dados de Playoffs ainda não disponíveis para uma das equipes."

    # 2. Lógica de Predição: Win Probability baseada em Net Rating
    # Historicamente, times com Net Rating superior em Playoffs vencem 78% das séries
    diff = metrics_a['net_rating'] - metrics_b['net_rating']
    prob_a = 50 + (diff * 2.5) # Simplificação estatística para probabilidade
    prob_a = max(min(prob_a, 95), 5) # Limitar entre 5% e 95%

    print(f"--- Predição de Playoffs: {time_a} vs {time_b} ---")
    print(f"Net Rating {time_a}: {metrics_a['net_rating']}")
    print(f"Net Rating {time_b}: {metrics_b['net_rating']}")
    print(f"Probabilidade de {time_a} avançar: {prob_a:.1f}%")
    print(f"Probabilidade de {time_b} avançar: {100-prob_a:.1f}%")

# Exemplo de uso (Times que chegaram longe em 2023-24)
predicao_playoffs("Boston Celtics", "Dallas Mavericks")