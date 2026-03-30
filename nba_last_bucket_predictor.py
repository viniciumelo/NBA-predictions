import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerclutch
from sklearn.ensemble import GradientBoostingRegressor

# 1. Obter dados de "Clutch Time" (Momentos Decisivos)
print("Buscando dados de performance em momentos decisivos (Clutch)...")
clutch_stats = leaguedashplayerclutch.LeagueDashPlayerClutch(
    season='2023-24', 
    clutch_time_nullable='Last 5 Minutes', 
    point_diff_nullable='5'
)
df_clutch = clutch_stats.get_data_frames()[0]

# 2. Engenharia de Variáveis para o "Último Ponto"
# Fatores: Pontos totais no clutch, Aproveitamento de lances livres (FT%) 
# e Taxa de Uso (Usage)
df_clutch['CLUTCH_EFFICIENCY'] = (df_clutch['PTS'] * df_clutch['FT_PCT']) + df_clutch['FGM']

# 3. Preparando o Modelo de Predição
# Jogadores que cobram lances livres e tentam mais arremessos no fim têm vantagem
features = ['PTS', 'FGM', 'FT_PCT', 'FGA', 'FTA']
X = df_clutch[features].fillna(0)
y = df_clutch['CLUTCH_EFFICIENCY'].fillna(0)

# Modelo Gradient Boosting para capturar quem "decide" sob pressão
model = GradientBoostingRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# 4. Gerando o Score de "Last Scorer"
df_clutch['LAST_BUCKET_SCORE'] = model.predict(X)

# 5. Filtrar os Top 5 Candidatos a fechar o jogo
# Filtramos jogadores com pelo menos 10 jogos em situações de clutch
top_closers = df_clutch[df_clutch['GP'] > 10].sort_values(by='LAST_BUCKET_SCORE', ascending=False).head(5)

