import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats

def calcular_probabilidade_vitoria(rating_casa, rating_fora):
    diff = rating_fora - rating_casa
    return 1 / (10**(diff / 400) + 1)

