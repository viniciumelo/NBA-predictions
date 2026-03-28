import pandas as pd
import numpy as np
from nba_api.stats.endpoints import leaguedashplayerstats
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# 1. Obter dados da temporada atual
print("Coletando dados de performance e carga de trabalho...")
pd.options.display.max_columns = None
stats = leaguedashplayerstats.LeagueDashPlayerStats(season='2023-24')
df = stats.get_data_frames()[0]

# 2. Engenharia de Variáveis para Risco de Lesão
# Criamos um "Score de Fadiga" baseado em Minutos, Idade (estimada) e Uso
# Nota: A API não fornece idade diretamente neste endpoint, então focamos em carga.
df['MIN_PER_GAME'] = df['MIN'] / df['GP']
df['TURNOVER_RATE'] = df['TOV'] / df['GP'] # Proxy para fadiga mental/física

# 3. Simulação de um "Target" de Lesão para Treinamento
# Na vida real, você usaria o histórico de lesões (IL). 
# Aqui, criamos um modelo de probabilidade baseado em desgaste (Overload).
features = ['MIN_PER_GAME', 'FGA', 'TOV', 'PF'] # Variáveis de esforço e contato
X = df[features].fillna(0)

# Normalização (Essencial para modelos de saúde/risco)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

