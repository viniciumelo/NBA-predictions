import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats
from nba_api.stats.static import teams

def get_offensive_metrics():
    # Puxa estatísticas avançadas de todas as equipes
    stats = leaguedashteamstats.LeagueDashTeamStats(
        measure_type_detailed_defense='Advanced',
        per_mode_detailed='PerGame'
    ).get_data_frames()[0]
    
    # Colunas: Nome, Rating Ofensivo, True Shooting %, Assist Ratio e % de Turnovers
    cols = ['TEAM_NAME', 'OFF_RATING', 'TS_PCT', 'AST_PCT', 'TM_TOV_PCT']
    return stats[cols]

def predict_offensive_superiority(team_a_name, team_b_name):
    df = get_offensive_metrics()
    
    team_a = df[df['TEAM_NAME'].str.contains(team_a_name, case=False)]
    team_b = df[df['TEAM_NAME'].str.contains(team_b_name, case=False)]
    
    if team_a.empty or team_b.empty:
        print("Erro: Uma das equipes não foi encontrada.")
        return

    # Extração de valores
    off_a, ts_a = team_a.iloc[0]['OFF_RATING'], team_a.iloc[0]['TS_PCT']
    off_b, ts_b = team_b.iloc[0]['OFF_RATING'], team_b.iloc[0]['TS_PCT']
    
    print(f"--- Comparativo Ofensivo: {team_a.iloc[0]['TEAM_NAME']} vs {team_b.iloc[0]['TEAM_NAME']} ---")
    print(f"{team_a.iloc[0]['TEAM_NAME']}: Rating {off_a} | Eficiência Real {ts_a:.1%}")
    print(f"{team_b.iloc[0]['TEAM_NAME']}: Rating {off_b} | Eficiência Real {ts_b:.1%}")
    
    # Lógica de Predição
    if off_a > off_b:
        winner = team_a.iloc[0]['TEAM_NAME']
        diff = off_a - off_b
    else:
        winner = team_b.iloc[0]['TEAM_NAME']
        diff = off_b - off_a
        
    print(f"\nPredição: O {winner} tem a maior força ofensiva.")
    print(f"Vantagem estimada de {diff:.2f} pontos a cada 100 posses.")
