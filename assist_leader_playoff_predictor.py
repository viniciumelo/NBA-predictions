import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats
from nba_api.stats.static import players

def get_playmaker_stats():
    # Coleta estatísticas de todos os jogadores ativos em 2025-26
    stats = leaguedashplayerstats.LeagueDashPlayerStats(season='2025-26').get_data_frames()[0]
    
    # Filtra jogadores com média alta de assistências (ex: > 7.0 AST/G)
    top_playmakers = stats[stats['AST'] > 7.0].sort_values(by='AST', ascending=False)
    
    return top_playmakers.head(10)

def predict_assist_leader():
    top_players = get_playmaker_stats()
    
    print(f"--- Top Playmakers: Média de Assistências (2025-26) ---")
    print(top_players[['PLAYER_NAME', 'AST', 'GP']].to_string(index=False))
    
    print("\n--- Metodologia de Predição ---")
    print("Para prever o líder total de assistências nos playoffs, consideramos:")
    print("1. Média de AST/G na temporada regular.")
    print("2. Probabilidade de avançar de fase (Séries de 7 jogos).")
    print("3. Estabilidade do sistema ofensivo.")
    
    # Exemplo de lógica de predição:
    # Lider = Max(AST_G * Numero_Estimado_de_Jogos_Playoff)
    print("\nLíder provável (Cenário atual): Nikola Jokic ou Luka Doncic")
    print("Motivo: Alta carga de posse de bola e probabilidade de séries longas.")

if __name__ == "__main__":
    predict_assist_leader()