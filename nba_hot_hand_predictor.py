import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats
from sklearn.ensemble import GradientBoostingRegressor

# 1. Obter estatísticas detalhadas da temporada atual
print("Buscando dados da NBA...")
stats = leaguedashplayerstats.LeagueDashPlayerStats(season='2023-24') # Ajuste a temporada se necessário
df = stats.get_data_frames()[0]

# 2. Engenharia de Dados para "Sequências"
# Criamos uma métrica baseada em FG_PCT (precisão) e FGM (cestas por jogo)
# Jogadores com alto FG% e muitos arremessos no garrafão têm maior chance de cestas seguidas.
df['EFICIENCIA_PROX_ARO'] = (df['FG_PCT'] * df['FGM']) / (df['FGA'] + 1)

# 3. Preparando o Modelo
# Features: Precisão de quadra, Precisão de lance livre e volume de cestas
features = ['FG_PCT', 'FT_PCT', 'FGM', 'FG3_PCT']
X = df[features].fillna(0)
y = df['EFICIENCIA_PROX_ARO'].fillna(0)

# Usando Gradient Boosting para capturar relações não-lineares
model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3)
model.fit(X, y)

# 4. Gerando o Ranking de Probabilidade de "Hot Hand"
df['HOT_HAND_SCORE'] = model.predict(X)

