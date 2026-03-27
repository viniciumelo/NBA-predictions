import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats, leaguedashgs_v2
import numpy as np

# ==============================================================================
# CONFIGURAÇÃO DO DUELO
# Digite o nome exato dos dois pivôs que deseja comparar
# ==============================================================================
CENTER_A = "Nikola Jokic"
CENTER_B = "Joel Embiid"
# ==============================================================================

print(f"Analisando duelo de pivôs: {CENTER_A} vs {CENTER_B}...\n")

# 1. Obter Estatísticas Gerais de Arremesso (Temporada Atual)
# Usado para prever "Mais Cestas Seguidas"
print("Buscando dados de eficiência...")
stats = leaguedashplayerstats.LeagueDashPlayerStats(season='2023-24')
df_general = stats.get_data_frames()[0]

# 2. Obter Estatísticas de Jump Ball (Bola ao Alto)
# Usado para prever "Marca Primeiro"
print("Buscando dados de Jump Ball inicial...")
# O endpoint leaguedashgs_v2 contém dados de situações específicas
jump_stats = leaguedashgs_v2.LeagueDashGs_V2(season='2023-24', clutch_time_nullable='Last 5 Minutes')
df_jump = jump_stats.get_data_frames()[0]

# 3. Filtrar e Preparar Dados dos Jogadores Escolhidos
def get_player_data(player_name):
    # Dados Gerais
    gen_data = df_general[df_general['PLAYER_NAME'] == player_name]
    # Dados de Jump Ball (Aproximação usando clutch time jump balls ganhas)
    jump_data = df_jump[df_jump['PLAYER_NAME'] == player_name]
    
    if gen_data.empty:
        print(f"Erro: Jogador {player_name} não encontrado nas estatísticas gerais.")
        return None
    
    return {
        'name': player_name,
        'team': gen_data['TEAM_ABBREVIATION'].values[0],
        'fg_pct': gen_data['FG_PCT'].values[0],
        'fgm': gen_data['FGM'].values[0],
        # Simplificação: Probabilidade baseada no volume de jump balls que o jogador disputa e ganha
        # Na API oficial, dados de First Basket específicos são difíceis de obter diretamente sem Play-by-Play
        'jump_ball_win_prox': jump_data['W_PCT'].values[0] if not jump_data.empty else 0.5
    }

player_a_data = get_player_data(CENTER_A)
player_b_data = get_player_data(CENTER_B)

if not player_a_data or not player_b_data:
    exit()

# ==============================================================================
# LÓGICA DE PREDDIÇÃO
# ==============================================================================

# A. Predição: QUEM MARCA PRIMEIRO
# Fatores: Quem ganha a bola ao alto (jump_ball_win_prox) * Eficiência do time
# Como não temos eficiência do time na primeira posse, usamos a precisão do próprio pivô como peso.
score_first_a = player_a_data['jump_ball_win_prox'] * player_a_data['fg_pct']
score_first_b = player_b_data['jump_ball_win_prox'] * player_b_data['fg_pct']

# B. Predição: MAIS CESTAS SEGUIDAS (Métrica "Hot Hand")
# Fatores: Alto volume de cestas feitas (FGM) e alta precisão (FG%)
# Pivôs que jogam perto do aro tendem a ter vantagem aqui.
score_hot_a = player_a_data['fg_pct'] * player_a_data['fgm']
score_hot_b = player_b_data['fg_pct'] * player_b_data['fgm']

# ==============================================================================
# RESULTADOS
# ==============================================================================
print("-" * 50)
print(f"RESULTADO DA PREDIÇÃO (Modelo Estatístico Simples)")
print("-" * 50)

# Resultado 1: Marca Primeiro
if score_first_a > score_first_b:
    prob = (score_first_a / (score_first_a + score_first_b)) * 100
    print(f"Probabilidade de MARCAR PRIMEIRO: {CENTER_A} ({prob:.1f}%)")
else:
    prob = (score_first_b / (score_first_a + score_first_b)) * 100
    print(f"Probabilidade de MARCAR PRIMEIRO: {CENTER_B} ({prob:.1f}%)")

print("  (Fator principal: Vantagem estimada no Jump Ball inicial)")
print("-" * 30)

# Resultado 2: Cestas Seguidas
if score_hot_a > score_hot_b:
    print(f"Probabilidade de MAIS CESTAS SEGUIDAS: {CENTER_A}")
else:
    print(f"Probabilidade de MAIS CESTAS SEGUIDAS: {CENTER_B}")

print("  (Fator principal: Combinação de alto volume de cestas e precisão de quadra)")
print("-" * 50)