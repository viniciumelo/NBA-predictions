import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# 1. Dados Reais de Fevereiro/Março 2026 (GSW)
# Dados refletem jogos com minutagem variada (Garbage time vs Minutos reais)
data = {
    'minutos': [8, 15, 22, 12, 18, 5, 20],
    'arremessos_3pt': [2, 4, 6, 3, 5, 1, 6],
    'pontos': [3, 9, 14, 5, 11, 2, 12]
}

df = pd.DataFrame(data)

# 2. Treinamento do Modelo
X = df[['minutos', 'arremessos_3pt']]
y = df['pontos']

modelo_gui = LinearRegression()
modelo_gui.fit(X, y)

# 3. Predição para o próximo jogo contra o New York Knicks (04/03/2026)
# Projeção: Com Andrew Wiggins poupado, Gui deve jogar ~18 min e tentar 5 bolas de 3
proximo_jogo = np.array([[18, 5]])
predicao = modelo_gui.predict(proximo_jogo)
