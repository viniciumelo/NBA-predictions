import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats, playerdashptpass
from sklearn.linear_model import LinearRegression

# 1. Configuração de busca
SEASON = '2023-24'
print(f"Analisando métricas de passes para a temporada {SEASON}...")

# 2. Obter estatísticas gerais de assistências
stats = leaguedashplayerstats.LeagueDashPlayerStats(season=SEASON)
df_gen = stats.get_data_frames()[0]

# 3. Engenharia de Dados: Criando o "Assist Streak Score"
# AST: Assistências Reais
# TOV: Erros (muitos erros quebram a sequência)
# AST_RATIO: Eficiência de assistências por posses
df_gen['ASSIST_EFFICIENCY'] = (df_gen['AST'] / (df_gen['TOV'] + 1)) * df_gen['AST_RATIO']
