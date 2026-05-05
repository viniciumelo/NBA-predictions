import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats

def predict_sweep_candidate():
    # Coleta estatísticas avançadas das equipes na temporada 2025-26
    # O Net Rating é a melhor métrica para medir dominância (OffRating - DefRating)
    stats = leaguedashteamstats.LeagueDashTeamStats(
        season='2025-26',
        measure_type_detailed_defense='Advanced'
    ).get_data_frames()[0]
    
    # Selecionamos métricas que indicam potencial de "varrida"
    # 1. NET_RATING: Dominância geral
    # 2. W_PCT: Consistência de vitória
    df = stats[['TEAM_NAME', 'W_PCT', 'NET_RATING']].copy()
    
    # Criamos o Sweep Probability Index (SPI)
    # SPI = (Net Rating * 0.7) + (Win % * 30)
    # Um Net Rating acima de 8.0 indica uma equipe historicamente dominante
    df['SWEEP_PROB_INDEX'] = (df['NET_RATING'] * 0.7) + (df['W_PCT'] * 30)
    
    # Ordenar pelos candidatos mais dominantes
    candidates = df.sort_values(by='SWEEP_PROB_INDEX', ascending=False).head(5)
    
    print(f"=== ANÁLISE DE PROBABILIDADE DE VARRIDA (SWEEP) - PLAYOFFS 2026 ===")
    print(candidates.to_string(index=False))
    
    top_team = candidates.iloc[0]
    print(f"\nPREDIÇÃO DE DOMÍNIO:")
    print(f"A equipe com maior chance de varrer seu oponente na 1ª rodada é o {top_team['TEAM_NAME']}.")
    print(f"Fator Crítico: Net Rating de {top_team['NET_RATING']} indica que o time não dá chances de reação.")
