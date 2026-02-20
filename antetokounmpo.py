import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# 1. Dados Reais (Temporada 2025-26 - Logs de Janeiro/Fevereiro)
# Giannis tem um "piso" de pontos muito alto devido aos lances livres
data = {
    'minutos': [32, 31, 30, 22, 31, 34, 35, 29],
    'lances_livres_tentados': [16, 6, 12, 9, 14, 15, 13, 11],
    'pontos': [22, 19, 21, 21, 25, 33, 31, 28]
}

df = pd.DataFrame(data)

# 2. Engenharia de Features (Polinomial de grau 2)
X = df[['minutos', 'lances_livres_tentados']]
y = df['pontos']

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

modelo = LinearRegression()
modelo.fit(X_poly, y)

# 3. Predição para o retorno contra New Orleans Pelicans (20/02/2026)
# Estimativa de retorno cauteloso: 30 minutos e 10 lances livres
proximo_jogo = np.array([[30, 10]])
proximo_jogo_poly = poly.transform(proximo_jogo)
predicao = modelo.predict(proximo_jogo_poly)

