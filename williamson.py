import numpy as np

def simular_performance(nome_jogador, media_pts, desvio_padrao, meta, simulacoes=10000):
    # Gera 10.000 cenários baseados na distribuição normal do jogador
    resultados = np.random.normal(media_pts, desvio_padrao, simulacoes)
    
    # Calcula a probabilidade de atingir a meta
    sucessos = np.sum(resultados >= meta)
    probabilidade = (sucessos / simulacoes) * 100
    
    