import pandas as pd
from nba_api.stats.endpoints import leaguedashtreampops, leaguedashplayerstats

def predicao_mvp():
    # 1. Buscar estatísticas avançadas de todos os jogadores
    print("Coletando dados da temporada...")
    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2023-24', 
        measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    # 2. Filtrar jogadores com volume mínimo (ex: mais de 30 minutos por jogo)
    top_candidates = player_stats[player_stats['MIN'] > 30].copy()

    # 3. Fórmula do MVP Score (Ponderada)
    # A lógica: Eficiência (PIE) + Vitórias (W_PCT) + Volume de Pontos
    # O PIE (Player Impact Estimate) é a melhor métrica da NBA para o "geral"
    
    top_candidates['MVP_SCORE'] = (
        (top_candidates['PIE'] * 50) +        # Impacto individual
        (top_candidates['W_PCT'] * 30) +      # Sucesso do time
        (top_candidates['PTS'] * 0.5) +       # Volume de pontos
        (top_candidates['AST'] * 0.2)         # Criação de jogadas
    )

    # Ordenar pelos melhores scores
    ranking = top_candidates[['PLAYER_NAME', 'TEAM_ABBREVIATION', 'PTS', 'W_PCT', 'PIE', 'MVP_SCORE']]
    ranking = ranking.sort_values(by='MVP_SCORE', ascending=False).head(5)

    print("\n--- TOP 5 CANDIDATOS AO MVP (Predição I.A.) ---")
    for i, row in ranking.iterrows():
        print(f"{row['PLAYER_NAME']} ({row['TEAM_ABBREVIATION']}) - Score: {row['MVP_SCORE']:.2f}")
    
    return ranking

