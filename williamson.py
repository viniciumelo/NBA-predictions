import numpy as np

def simular_performance(nome_jogador, media_pts, desvio_padrao, meta, simulacoes=10000):
    # Gera 10.000 cenários baseados na distribuição normal do jogador
    resultados = np.random.normal(media_pts, desvio_padrao, simulacoes)
    
    # Calcula a probabilidade de atingir a meta
    sucessos = np.sum(resultados >= meta)
    probabilidade = (sucessos / simulacoes) * 100
    
    print(f"--- Predição para {nome_jogador} ---")
    print(f"Média da Temporada: {media_pts} pts")
    print(f"Meta de Pontos: {meta}")
    print(f"Probabilidade de bater a meta: {probabilidade:.2f}%")
    
    if probabilidade > 60:
        print("Palpite: Forte tendência de OVER (Acima).")
    elif probabilidade < 40:
        print("Palpite: Forte tendência de UNDER (Abaixo).")
    else:
        print("Palpite: Jogo arriscado, odds equilibradas.")

# Dados reais do Zion em Março/2026
# Média: 21.4 | Desvio padrão estimado: 4.5 (Zion é consistente, mas varia com minutos)
meta_do_dia = float(input("Qual a linha de pontos do Zion hoje (ex: 22.5)? "))
simular_performance("Zion Williamson", 21.4, 4.5, meta_do_dia)