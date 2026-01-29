import pandas as pd

def encontrar_winning_ticket_allstar():
    print("Iniciando Poda Iterativa para encontrar o 'Winning Ticket' do All-Star 2026...")

    # 1. A Rede Densa (Pool de Talentos)
    elencos = {
        'MUNDO': {
            'Jokic': 98, 'Doncic': 97, 'Giannis': 96, 
            'SGA': 95, 'Wembanyama': 94
        },
        'EUA': {
            'Curry': 90, 'Brunson': 89, 'Maxey': 91, 
            'Cunningham': 88, 'Brown': 89
        }
    }

    # 2. O Processo de Pruning (Poda)
    # Na LTH, removemos os pesos (jogadores) abaixo de um certo threshold de influência.
    def extrair_subrede_vencedora(time_dict, percentual_poda=0.4):
        # Ordenamos por impacto e removemos os 40% "menos eficientes" para o Clutch
        ordenado = sorted(time_dict.items(), key=lambda x: x[1], reverse=True)
        num_manter = int(len(ordenado) * (1 - percentual_poda))
        # O 'Winning Ticket' é a sub-rede que sobra
        return dict(ordenado[:num_manter + 1])

    sub_rede_mundo = extrair_subrede_vencedora(elencos['MUNDO'])
    sub_rede_eua = extrair_subrede_vencedora(elencos['EUA'])

    # 3. Cálculo de Potencial do Bilhete (Winning Ticket Potential)
    score_mundo = sum(sub_rede_mundo.values()) / len(sub_rede_mundo)
    score_eua = sum(sub_rede_eua.values()) / len(sub_rede_eua)

    # 4. Predição Final
    prob_mundo = (score_mundo / (score_mundo + score_eua)) * 100

    print(f"\n--- RESULTADO DA PODA (SUB-REDES ISOLADAS) ---")
    print(f"Bilhete Mundo (Núcleo): {list(sub_rede_mundo.keys())}")
    print(f"Bilhete EUA (Núcleo): {list(sub_rede_eua.keys())}")
    
    print(f"\n--- PREDIÇÃO FINAL (BASEADA NO WINNING TICKET) ---")
    print(f"Probabilidade de Vitória MUNDO: {prob_mundo:.2f}%")
    print(f"Veredito: A sub-rede do Mundo (Jokic/Doncic) tem pesos iniciais muito superiores.")

encontrar_winning_ticket_allstar()