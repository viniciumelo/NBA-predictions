import pandas as pd
from nba_api.stats.endpoints import playercareerstats

def predict_jokic_next_season():
    # ID fixo de Nikola Jokić na NBA API
    jokic_id = 203999
    
    print("Buscando histórico de carreira de Nikola Jokic...")
    career = playercareerstats.PlayerCareerStats(player_id=jokic_id)
    df_totals = career.get_data_frames()[0]
    
    # Filtrar apenas temporada regular
    df_reg = df_totals[df_totals['WHEN_MADE'] == 'Regular Season'].copy()
    
    if df_reg.empty:
        df_reg = df_totals
        
    # Calcular médias por jogo históricas
    df_reg['PPG'] = df_reg['PTS'] / df_reg['GP']
    df_reg['APG'] = df_reg['AST'] / df_reg['GP']
    df_reg['RPG'] = df_reg['REB'] / df_reg['GP']
    df_reg['MPG'] = df_reg['MIN'] / df_reg['GP']
    
    # Pegar as últimas 3 temporadas para analisar o "padrão MVP" recente
    recent_seasons = df_reg.tail(3)
    
    if len(recent_seasons) < 3:
        print("Dados históricos insuficientes para calcular a tendência.")
        return

    # Pesos para a média móvel (dando maior importância à temporada mais recente)
    # Pesos: T-2 (20%), T-1 (30%), Temporada Atual (50%)
    weights = [0.2, 0.3, 0.5]
    
    projected_pts = sum(recent_seasons['PPG'] * weights)
    projected_ast = sum(recent_seasons['APG'] * weights)
    projected_reb = sum(recent_seasons['RPG'] * weights)
    projected_min = sum(recent_seasons['MPG'] * weights)
    
    # --- Fator de Ajuste de Longevidade (Gestão de Carga) ---
    # Para preservar Jokić para os playoffs à medida que envelhece, 
    # projetamos uma leve redução de 2% no ritmo de minutos, mas mantendo a eficiência.
    longevity_factor_mins = 0.98
    longevity_factor_stats = 0.99 # Redução marginal por ritmo
    
    final_min = projected_min * longevity_factor_mins
    final_pts = projected_pts * longevity_factor_stats
    final_ast = projected_ast * longevity_factor_stats
    final_reb = projected_reb * longevity_factor_stats
    
    print("\n" + "="*60)
    print("PROJEÇÃO DE DESEMPENHO: NIKOLA JOKIĆ (2026/27)")
    print("="*60)
    print(f"Minutos Projetados: {final_min:.1f} MPG")
    print("-" * 60)
    print(f"PONTOS:      {final_pts:.1f} PTS/G")
    print(f"ASSISTÊNCIAS: {final_ast:.1f} AST/G")
    print(f"REBOTES:     {final_reb:.1f} REB/G")
    print("-" * 60)
    print(f"Projeção de Triplos-Duplos: Quase uma média de Triple-Double!")
    print("Metodologia: Média móvel ponderada com ajuste de longevidade.")
    print("="*60)

if __name__ == "__main__":
    predict_jokic_next_season()