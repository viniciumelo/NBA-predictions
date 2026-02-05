import pandas as pd
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog

def encontrar_bilhete_premiado_pts(nome_jogador):
    print(f"Buscando a sub-rede vencedora para {nome_jogador}...")
    
   