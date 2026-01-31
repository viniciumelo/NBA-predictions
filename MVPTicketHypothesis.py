import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def predicao_mvp_lottery_ticket():
    print("Iniciando Poda Iterativa para isolar o 'Winning Ticket' do MVP 2026...")
    
    # 1. Coleta da Rede Densa (Todos os jogadores)
    # Usamos Advanced Stats para capturar a 'arquitetura' real do impacto
    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26', 
        measure_type_detailed_advanced='Advanced'
    ).get_data_frames()[0]

    # 2. O Processo de Poda (Pruning)
    # Removemos neurônios (jogadores) com baixa magnitude de impacto
    # Um 'Winning Ticket' precisa de volume (USG_PCT) e eficiência (NET_RATING)
    threshold_min = 32
    threshold_usg = player_stats['USG_PCT'].median()
    
    # Poda: Mantemos apenas a sub-rede de alto uso e alta minutagem
    sub_rede = player_stats[
        (player_stats['MIN'] >= threshold_min) & 
        (player_stats['USG_PCT'] >= threshold_usg)
    ].copy()

    # 3. Identificação do Bilhete Premiado (MVP Score)
    # A métrica foca na estabilidade da performance (PIE + E_OFF_RATING)
    # O MVP Score aqui é a 'probabilidade de convergência' do jogador ao título
    sub_rede['MVP_TICKET_SCORE'] = (
        (sub_rede['PIE'] * 100) +        # Magnitude do Impacto
        (sub_rede['OFF_RATING'] * 0.2) +  # Eficiência da Conexão Ofensiva
        (sub_rede['W_PCT'] * 50)          # Recompensa por Vitória da Rede (Time)
    )

    # 4. Isolando os Vencedores da Loteria
    ranking = sub_rede.sort_values(by='MVP_TICKET_SCORE', ascending=False).head(5)

    print("\n--- SUB-REDES IDENTIFICADAS (WINNING TICKETS PARA MVP) ---")
    for rank, (i, row) in enumerate(ranking.iterrows(), 1):
        print(f"Bilhete #{rank}: {row['PLAYER_NAME']} [{row['TEAM_ABBREVIATION']}]")
        print(f"   > Estabilidade (PIE): {row['PIE']:.1%}")
        print(f"   > MVP Ticket Score: {row['MVP_TICKET_SCORE']:.2f}\n")
    
    return ranking

if __name__ == "__main__":
    predicao_mvp_lottery_ticket()