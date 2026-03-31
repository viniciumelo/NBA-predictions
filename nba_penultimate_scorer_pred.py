import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerclutch
from sklearn.ensemble import RandomForestRegressor

# 1. Buscar dados de Clutch (Últimos 5 min, diferença de até 5 pontos)
print("Analisando dados de momentos decisivos da NBA...")
clutch_stats = leaguedashplayerclutch.LeagueDashPlayerClutch(
    season='2023-24', 
    clutch_time_nullable='Last 5 Minutes', 
    point_diff_nullable='5'
)
df_clutch = clutch_stats.get_data_frames()[0]

# 2. Lógica para o "Penúltimo Ponto"
# O penúltimo ponto geralmente pertence a:
# A) Quem bate muitos lances livres (FTA)
# B) Quem tem alto volume de arremessos (FGA) mas não necessariamente a maior eficiência final
df_clutch['PENULTIMATE_SCORE_INDEX'] = (df_clutch['FTA'] * 0.6) + (df_clutch['FGA'] * 0.4)

# 3. Modelo de Regressão
features = ['FTA', 'FGA', 'PTS', 'FT_PCT', 'USG_PCT']
X = df_clutch[features].fillna(0)
y = df_clutch['PENULTIMATE_SCORE_INDEX'].fillna(0)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# 4. Predição
df_clutch['PROB_PENULTIMATE'] = model.predict(X)

# 5. Ranking dos Candidatos
# Filtramos jogadores com participação ativa (GP > 10 no clutch)
top_candidates = df_clutch[df_clutch['GP'] > 10].sort_values(by='PROB_PENULTIMATE', ascending=False).head(5)

print("\n" + "="*60)
print("PREDIÇÃO: ATLETAS MAIS PROVÁVEIS PARA O PENÚLTIMO PONTO")
print("="*60)

for i, row in top_candidates.iterrows():
    # Normalização visual do score
    score = (row['PROB_PENULTIMATE'] / top_candidates['PROB_PENULTIMATE'].max()) * 100
    print(f"Atleta: {row['PLAYER_NAME']} ({row['TEAM_ABBREVIATION']})")
    print(f"Volume no Clutch (FGA+FTA): {row['FGA'] + row['FTA']:.1f} | Índice de Probabilidade: {score:.1f}%")
    print("-" * 40)