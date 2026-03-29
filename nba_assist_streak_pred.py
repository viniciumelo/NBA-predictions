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

# 4. Preparação do Modelo (Predição baseada em volume e precisão)
# Vamos prever a chance de "Sequência" usando Volume de Assistências e Minutos
features = ['AST', 'MIN', 'AST_RATIO']
X = df_gen[features].fillna(0)
y = df_gen['ASSIST_EFFICIENCY'].fillna(0)

model = LinearRegression()
model.fit(X, y)

# 5. Aplicando a predição para encontrar o "Garçom" mais provável
df_gen['STREAK_PROBABILITY'] = model.predict(X)

# Filtrar apenas jogadores que jogam tempo relevante (mais de 20 min/jogo)
# e que tenham média alta de assistências
df_filtered = df_gen[df_gen['GP'] > 10].copy()
df_filtered['AST_PG'] = df_filtered['AST'] / df_filtered['GP']
top_playmakers = df_filtered[df_filtered['AST_PG'] > 5].sort_values(by='STREAK_PROBABILITY', ascending=False).head(5)

# 6. Exibição dos resultados
print("\n" + "="*50)
print("PREDIÇÃO: MAIOR PROBABILIDADE DE ASSISTÊNCIAS SEGUIDAS")
print("="*50)

