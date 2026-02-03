import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats

def encontrar_bilhete_premiado_faltas():
    print("Iniciando Poda Iterativa para isolar a sub-rede de agressividade coletiva...")
    
    # 1. Coleta da 'Rede Densa' (Estatísticas Base e Avançadas)
    team_base = leaguedashteamstats.LeagueDashTeamStats(
        season='2025-26', measure_type_detailed_advanced='Base'
    ).get_data_frames()[0]

    team_adv = leaguedashteamstats.LeagueDashTeamStats(
        season='2025-26', measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    df = pd.merge(team_base[['TEAM_ID', 'TEAM_NAME', 'PF', 'GP']], 
                  team_adv[['TEAM_ID', 'PACE', 'DEF_RATING', 'PCT_AST']], on='TEAM_ID')

    # 2. O Processo de Poda (Pruning)
    # Removemos neurônios (times) que não têm "magnitude" defensiva problemática.
    # O Bilhete Premiado de faltas geralmente está em times com DEF_RATING acima da média.
    threshold_defensivo = df['DEF_RATING'].mean()
    
    # Poda: Mantemos apenas a sub-rede de times com defesa vulnerável
    sub_rede = df[df['DEF_RATING'] >= threshold_defensivo].copy()

    # 3. Identificação do Winning Ticket (Foul Potential Score)
    # Na LTH, o 'Winning Ticket' tem pesos iniciais que favorecem o resultado.
    # Aqui, o resultado é a falta. O peso é o PACE (exposição) e a deficiência (DEF_RATING).
    sub_rede['WINNING_TICKET_SCORE'] = (
        (sub_rede['PF'] * 0.5) +               # Frequência observada
        (sub_rede['DEF_RATING'] * 0.4) +        # Vulnerabilidade estrutural
        (sub_rede['PACE'] * 0.1)                # Fator de aceleração (exposição)
    )

    # 4. Resultado: Os 5 Bilhetes Premiados (Times com maior risco estrutural)
    ranking = sub_rede.sort_values(by='WINNING_TICKET_SCORE', ascending=False).head(5)

    print("\n--- SUB-REDE IDENTIFICADA: WINNING TICKETS DE FALTAS ---")
    for _, row in ranking.iterrows():
        print(f"Time: {row['TEAM_NAME']}")
        print(f" > Ticket Score (Potencial): {row['WINNING_TICKET_SCORE']:.2f}")
        print(f" > Arquitetura: Pace {row['PACE']} | Def Rating {row['DEF_RATING']}\n")
    
    return ranking

if __name__ == "__main__":
    encontrar_bilhete_premiado_faltas()