import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predicao_faltas_allstar():
    print("Analisando perfil disciplinar para o All-Star Game...")
    
    # 1. Coletar dados da temporada (ano atual 2026)
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        measure_type_detailed_advanced='Base'
    ).get_data_frames()[0]

    # 2. Filtrar apenas os prováveis All-Stars (jogadores de alto impacto)
    # Focamos em jogadores com PIE alto e que jogam muitos minutos
    all_star_pool = stats[stats['PIE'] > 0.13].copy()

    # 3. Cálculo do 'Aggression Score'
    # Faltas por 36 minutos + Taxa de Tocos (indica tentativa de contestar chutes)
    all_star_pool['PF_PER_36'] = (all_star_pool['PF'] / all_star_pool['MIN']) * 36
    all_star_pool['FOUL_PROB'] = (all_star_pool['PF_PER_36'] * 0.7) + (all_star_pool['BLK'] * 0.3)

    ranking = all_star_pool[['PLAYER_NAME', 'TEAM_ABBREVIATION', 'PF_PER_36', 'FOUL_PROB']]
    ranking = ranking.sort_values(by='FOUL_PROB', ascending=False).head(5)

    print("\n--- JOGADORES COM MAIOR CHANCE DE COMETER FALTAS (ALL-STAR) ---")
    for i, row in ranking.iterrows():
        # No All-Star, o número de faltas é baixo (geralmente 1 ou 2 lideram)
        print(f"{row['PLAYER_NAME']} | Risco de 'Foul-Out' Festivo: {row['FOUL_PROB']:.1f}")
    
    return ranking

predicao_faltas_allstar()