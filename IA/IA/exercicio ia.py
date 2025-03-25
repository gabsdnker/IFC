import numpy as np
import matplotlib.pyplot as plt

# Número de pontos N
N = 10

# Gerar pontos aleatórios (x_i,y_i)
np.random.seed(42) # Para manteros resultados reprodutíveis
x = np.linspace(-5, 5, N) # Posições x igualmente espaçadas 
y = np.random.uniform(-10, 10, N) # Valores aleatórios para y

# Ajustar um plonômio de grau N-1
coef = np.polyfit(x, y, N-1) # Encontra os  coeficientes do polinômio
polinomio = np.poly1d(coef) # Cia a função polinomial

# Cria pontos para plotagem do polinômio
x_plot = np.linspace(-6, 6, 100)
y_plot = polinomio(x_plot)

# Plotar os pontos e a curva ajustada 
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='red', label= 'Pontos (x_i, y_i)')
plt.plot(x_plot, y_plot, label= f'Polinomio de grau {N-1}', color='black')
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Ajuste de Polinomio com {N} pontos')
plt.legend()
plt.grid()
plt.show()