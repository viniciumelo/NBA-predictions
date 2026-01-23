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

    # 3. Cálculo de Força
    forca_mundo = sum([scores[p] for p in time_mundo]) / len(time_mundo)
    forca_eua = sum([scores[p] for p in time_eua_pool]) / len(time_eua_pool)

    # 4. Probabilidade Ajustada
    # O Time Mundo leva vantagem histórica pela química e tamanho (Wemby + Jokic + Giannis)
    prob_mundo = (forca_mundo / (forca_mundo + forca_eua)) * 100

    print(f"--- PREDIÇÃO ALL-STAR GAME 2026 (LA) ---")
    print(f"Probabilidade Time MUNDO: {prob_mundo:.1f}%")
    print(f"Probabilidade Times EUA: {100 - prob_mundo:.1f}%")
    print(f"\nFator Decisivo: O 'Frontcourt' do Mundo (Jokic/Wemby/Giannis) é imparável.")
