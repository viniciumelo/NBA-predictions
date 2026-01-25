import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

def encontrar_bilhete_premiado_nba():
    print("Iniciando busca pelo 'Bilhete de Loteria' (Atiradores de Elite)...")
    
    # 1. Coleta de dados (A 'Rede Inicial')
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season='2025-26',
        measure_type_detailed_advanced='Base'
    ).get_data_frames()[0]

    # 2. O Processo de Podagem (Pruning)
    # Em vez de um filtro simples, removemos as "conexões fracas" (baixa amostragem e instabilidade)
    media_tentativas = stats['FG3A'].mean()
    
    # Mantemos apenas jogadores acima da média de tentativas da liga (Filtro de Relevância)
    sub_rede = stats[stats['FG3A'] > media_tentativas].copy()

    # 3. Identificação do 'Winning Ticket'
    # Aplicamos uma métrica de eficiência ajustada ao risco
    # A lógica: Volume alto com eficiência constante é o bilhete premiado.
    sub_rede['LOTTERY_SCORE'] = (
        (sub_rede['FG3M'] * 0.7) +  # Valorizamos a entrega real
        (sub_rede['FG3_PCT'] * 15)  # Intensificamos o peso da precisão
    )

    # 4. Isolando os vencedores
    top_vencedores = sub_rede.sort_values(by='LOTTERY_SCORE', ascending=False).head(5)

    print(f"\n--- OS 5 BILHETES PREMIADOS DA RODADA ---")
    for _, player in top_vencedores.iterrows():
        print(f"ID: {player['PLAYER_ID']} | {player['PLAYER_NAME']} [{player['TEAM_ABBREVIATION']}]")
        print(f"   > Score de Estabilidade: {player['LOTTERY_SCORE']:.2f}")
        print(f"   > Eficiência: {player['FG3_PCT']:.1%} em {player['FG3A']} tentativas\n")
    
    return top_vencedores