import pandas as pd
from nba_api.stats.endpoints import playercareerstats

def predict_sga_next_season():
    # ID fixo do Shai Gilgeous-Alexander na NBA API
    sga_id = 1628983
    
    print("Buscando histórico de carreira de SGA...")
    career = playercareerstats.PlayerCareerStats(player_id=sga_id)
    df_totals = career.get_data_frames()[0]
    
    # Filtrar apenas temporada regular
    df_reg = df_totals[df_totals['WHEN_MADE'] == 'Regular Season'].copy()
    
    if df_reg.empty:
        # Alternativa caso o filtro mude na API
        df_reg = df_totals
        
    # Calcular médias por jogo históricas
    df_reg['PPG'] = df_reg['PTS'] / df_reg['GP']
    df_reg['APG'] = df_reg['AST'] / df_reg['GP']
    df_reg['RPG'] = df_reg['REB'] / df_reg['GP']
    df_reg['MPG'] = df_reg['MIN'] / df_reg['GP']
    
    # Pegar as últimas 3 temporadas para analisar a tendência recente de elite
    recent_seasons = df_reg.tail(3)
    
    if len(recent_seasons) < 3:
        print("Dados históricos insuficientes para calcular a tendência.")
        return

    # Pesos para a média móvel (dando mais importância para a consistência mais recente)
    weights = [0.2, 0.3, 0.5]
    
    projected_pts = sum(recent_seasons['PPG'] * weights)
    projected_ast = sum(recent_seasons['APG'] * weights)
    projected_reb = sum(recent_seasons['RPG'] * weights)
    projected_min = sum(recent_seasons['MPG'] * weights)
    
    # --- Fator de Ajuste de Maturidade (Prime Anos) ---
    # Como SGA já está no auge, aplicamos um fator de estabilização técnica (+1% de eficiência)
    prime_factor = 1.01
    
    final_pts = projected_pts * prime_factor
    final_ast = projected_ast * prime_factor
    final_reb = projected_reb * prime_factor
    
    print("\n" + "="*60)
    print("PROJEÇÃO DE DESEMPENHO: SHAI GILGEOUS-ALEXANDER (2026/27)")
    print("="*60)
    print(f"Minutos Projetados: {projected_min:.1f} MPG")
    print("-" * 60)
    print(f"PONTOS:      {final_pts:.1f} PTS/G")
    print(f"ASSISTÊNCIAS: {final_ast:.1f} AST/G")
    print(f"REBOTES:     {final_reb:.1f} REB/G")
    print("-" * 60)
    print("Metodologia: Média móvel linear ponderada (últimos 3 anos)")
    print("Ajustado com Fator de Maturidade de Atleta de Elite.")
    print("="*60)

if __name__ == "__main__":
    predict_sga_next_season()