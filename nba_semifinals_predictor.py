import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats

def predict_semifinalists():
    # Coleta estatísticas avançadas das equipes na temporada 2025-26
    print("Buscando dados avançados da NBA...")
    team_stats = leaguedashteamstats.LeagueDashTeamStats(
        season='2025-26',
        measure_type_detailed_defense='Advanced'
    ).get_data_frames()[0]

    # Selecionar colunas essenciais para a predição
    # Net Rating é o melhor indicador de domínio de uma equipe
    cols = ['TEAM_NAME', 'TEAM_ID', 'NET_RATING', 'W_PCT', 'OFF_RATING', 'DEF_RATING']
    df = team_stats[cols]

    # Simular divisão por Conferência (Mapeamento manual necessário para precisão)
    east_teams = [
        "Boston Celtics", "Milwaukee Bucks", "New York Knicks", "Philadelphia 76ers",
        "Cleveland Cavaliers", "Indiana Pacers", "Orlando Magic", "Miami Heat",
        "Atlanta Hawks", "Brooklyn Nets", "Chicago Bulls", "Charlotte Hornets",
        "Detroit Pistons", "Toronto Raptors", "Washington Wizards"
    ]
    
    df['CONFERENCE'] = df['TEAM_NAME'].apply(lambda x: 'East' if x in east_teams else 'West')

    # Ranking baseado em Net Rating (Equipes com melhor equilíbrio ataque/defesa)
    # Playoffs são decididos pela capacidade de parar o adversário e converter posses críticas
    df_sorted = df.sort_values(by='NET_RATING', ascending=False)

    print("\n" + "="*60)
    print("PREDIÇÃO DE SEMIFINALISTAS (FINAIS DE CONFERÊNCIA 2026)")
    print("="*60)

    for conf in ['East', 'West']:
        print(f"\nCONFERÊNCIA {conf.upper()}:")
        top_4 = df_sorted[df_sorted['CONFERENCE'] == conf].head(4)
        
        # Simulando o cruzamento (Geralmente os 2 melhores Net Ratings se encontram na Final de Conf.)
        semifinalists = top_4['TEAM_NAME'].iloc[:2].tolist()
        
        for i, team in enumerate(semifinalists, 1):
            net_r = top_4[top_4['TEAM_NAME'] == team]['NET_RATING'].values[0]
            print(f"{i}º Candidato: {team} (Net Rating: {net_r})")

   

if __name__ == "__main__":
    predict_semifinalists()