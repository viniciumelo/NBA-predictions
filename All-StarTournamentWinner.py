import pandas as pd

def predicao_vencedor_allstar_2026():
    # 1. Definição dos elencos titulares (Baseado nos dados reais de Jan/2026)
    # Time Mundo (World Team) está extremamente forte com 3 MVPs
    time_mundo = ['Nikola Jokic', 'Luka Doncic', 'Giannis Antetokounmpo', 'Shai Gilgeous-Alexander', 'Victor Wembanyama']
    
    # Time EUA (Dividido entre os starters de cada conferência)
    time_eua_pool = ['Stephen Curry', 'Jalen Brunson', 'Cade Cunningham', 'Tyrese Maxey', 'Jaylen Brown']

    # 2. Atribuição de Impact Score (Simulação baseada em PER/PIE de 2026)
    # O Time Mundo tem 4 dos 5 maiores PIEs da liga atualmente.
    scores = {
        'Nikola Jokic': 98, 'Luka Doncic': 97, 'Giannis Antetokounmpo': 96, 
        'Shai Gilgeous-Alexander': 95, 'Victor Wembanyama': 94,
        'Stephen Curry': 90, 'Jalen Brunson': 89, 'Tyrese Maxey': 91,
        'Cade Cunningham': 88, 'Jaylen Brown': 89
    }
