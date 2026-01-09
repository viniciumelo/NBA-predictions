import pandas as pd
from nba_api.stats.endpoints import leaguegamefinder

def calcular_probabilidade_vitoria(rating_casa, rating_fora):
    # O fator 400 é o padrão do sistema Elo
    diff = rating_fora - rating_casa
    prob_casa = 1 / (10**(diff / 400) + 1)
    return prob_casa

def analise_equipe_vencedora(time_home, time_away):
    # 1. Coletar dados de jogos recentes (Exemplo simplificado de lógica)
    # Na prática, você iteraria sobre a temporada para construir os ratings
    gamefinder = leaguegamefinder.LeagueGameFinder(season_nullable='2023-24')
    games = gamefinder.get_data_frames()[0]

    # 2. Definição de Ratings Iniciais (Média da liga = 1500)
    # Em um modelo real, você calcularia isso jogo a jogo
    ratings = {
        "Boston Celtics": 1650, # Exemplo de time forte
        "Golden State Warriors": 1580,
        "Detroit Pistons": 1350, # Exemplo de time em reconstrução
        "Los Angeles Lakers": 1550
    }

    # Pegar ratings dos times selecionados (ou padrão 1500 se não listado)
    r_casa = ratings.get(time_home, 1500) + 50 # +50 de bônus por jogar em casa
    r_fora = ratings.get(time_away, 1500)

    prob = calcular_probabilidade_vitoria(r_casa, r_fora)

    print(f"--- Análise de Confronto: {time_home} vs {time_away} ---")
    print(f"Rating {time_home} (c/ bônus casa): {r_casa}")
    print(f"Rating {time_away}: {r_fora}")
    print(f"Probabilidade de vitória do {time_home}: {prob:.2%}")
    print(f"Probabilidade de vitória do {time_away}: {1-prob:.2%}")

# Teste de Predição
analise_equipe_vencedora("Boston Celtics", "Los Angeles Lakers")