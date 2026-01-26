import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats

def encontrar_bilhete_vencedor_clutch():
    print("Executando poda de dados para isolar a sub-rede vencedora (4º Quarto)...")
    
    # 1. Coleta da 'Rede Densa' (Dados Base + Avançados)
    # Filtramos apenas o 4º período para remover o ruído dos quartos iniciais
    base_4q = leaguedashteamstats.LeagueDashTeamStats(
        season='2025-26', period_nullable=4, measure_type_detailed_advanced='Base'
    ).get_data_frames()[0]

    adv_4q = leaguedashteamstats.LeagueDashTeamStats(
        season='2025-26', period_nullable=4, measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    # Unificação focada em métricas de intensidade
    df = pd.merge(base_4q, adv_4q[['TEAM_ID', 'PACE', 'OFF_RATING', 'TS_PCT']], on='TEAM_ID')

    # 2. O Processo de Poda (Pruning)
    # Um 'Bilhete de Loteria' não é apenas quem marca muito, mas quem é eficiente no caos.
    # Vamos criar um Score de Estabilidade (Winning Ticket Score)
    # Valorizamos: Eficiência (OFF_RATING) e Precisão Real (TS_PCT) ajustados ao Volume (PTS)
    
    df['CLUTCH_TICKET_SCORE'] = (
        (df['OFF_RATING'] * 0.5) + # Eficiência pura
        (df['TS_PCT'] * 100) +      # Qualidade do arremesso sob pressão
        (df['PTS'] * 0.3)          # Volume de entrega
    )

    # 3. Isolando os 'Winning Tickets'
    # Ordenamos para encontrar os times que "ganharam na loteria" da consistência final
    ranking = df[['TEAM_NAME', 'PTS', 'OFF_RATING', 'TS_PCT', 'CLUTCH_TICKET_SCORE']]
    ranking = ranking.sort_values(by='CLUTCH_TICKET_SCORE', ascending=False).head(5)

    print("\n--- IDENTIFICAÇÃO DOS BILHETES PREMIADOS (TOP 5 CLUTCH) ---")
    for _, row in ranking.iterrows():
        print(f"Time: {row['TEAM_NAME']}")
        print(f" > Ticket Score: {row['CLUTCH_TICKET_SCORE']:.2f}")
        print(f" > Eficiência Real: {row['TS_PCT']:.1%} | Ortg: {row['OFF_RATING']}\n")
    
    return ranking