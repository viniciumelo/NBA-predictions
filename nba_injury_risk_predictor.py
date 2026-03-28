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

