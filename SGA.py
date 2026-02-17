import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 1. Dados reais simplificados do SGA (Temporada 2025-26)
# Simulando logs de jogos recentes (Minutos vs Pontos)
data = {
    'minutos': [28, 33, 31, 36, 35, 38, 34, 32],
    'pontos': [20, 34, 30, 29, 24, 37, 31, 28]
}

df = pd.DataFrame(data)

# 2. Preparação do Modelo
X = df[['minutos']] # Variável independente
y = df['pontos']    # Variável alvo (o que queremos prever)

modelo = LinearRegression()
modelo.fit(X, y)

# 3. Predição para o próximo jogo
# Vamos supor que ele jogue 36 minutos (sua média de tempo em jogos apertados)
minutos_proximo_jogo = np.array([[36]])
predicao = modelo.predict(minutos_proximo_jogo)

print(f"--- Predição para SGA ---")
print(f"Minutos projetados: {minutos_proximo_jogo[0][0]}")
print(f"Pontuação prevista: {predicao[0]:.2f} pontos")

# 4. Visualização da Tendência
plt.scatter(X, y, color='blue', label='Jogos Reais')
plt.plot(X, modelo.predict(X), color='red', label='Tendência (Regressão)')
plt.xlabel('Minutos em Quadra')
plt.ylabel('Pontos Marcados')
plt.title('Relação Minutos x Pontos: SGA 2026')
plt.legend()
plt.show()