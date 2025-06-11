import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold
from math import sqrt
import numpy as np


# 1. Leitura do arquivo CSV
df = pd.read_csv('Users/gabrielli.danker/Documents/GitHub/IFC/IA/Séries Temporais/RAIZ4.csv')


# 2. Converter coluna Date (MM/DD/YYYY)
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')


# 3. Ordenar por data crescente (importante para séries temporais)
df = df.sort_values('Date').reset_index(drop=True)


# 4. Definir X (entrada) e y (target)
X = df[['Open']].values
y = df['Price'].values


# 5. Separar dados em treino e teste (70% treino, 30% teste)
split_idx = int(0.7 * len(df))
X_train, X_test = X[:split_idx], X[split_idx:]
y_train, y_test = y[:split_idx], y[split_idx:]


# 6. K-Fold Cross Validation no treino
kf = KFold(n_splits=10, shuffle=True, random_state=42)
rmse_scores = []


for train_index, val_index in kf.split(X_train):
  X_train_fold, X_val_fold = X_train[train_index], X_train[val_index]
  y_train_fold, y_val_fold = y_train[train_index], y_train[val_index]


  modelo = LinearRegression()
  modelo.fit(X_train_fold, y_train_fold)
  y_pred_val = modelo.predict(X_val_fold)


  rmse = sqrt(mean_squared_error(y_val_fold, y_pred_val))
  rmse_scores.append(rmse)


print(f'RMSE médio (K-Fold treino): {np.mean(rmse_scores):.4f}')


# 7. Treinar modelo final com todo treino
modelo_final = LinearRegression()
modelo_final.fit(X_train, y_train)


# 8. Prever no conjunto de teste
y_pred_test = modelo_final.predict(X_test)
rmse_test = sqrt(mean_squared_error(y_test, y_pred_test))
print(f'RMSE no teste: {rmse_test:.4f}')


# 10. Previsão para próximos 5 dias (exemplo de aberturas futuras)
# Você precisa preencher os valores reais de abertura para estes dias:
# novas_aberturas = np.array([[65.53], [67.07], [66.99], [64.03], [67.87]])  # Exemplo, ajuste conforme seu dado real
# novas_aberturas = np.array([[1.98], [1.94],[1.98],[2.01],[2.01]])


novas_aberturas = np.array([[2.01], [2.01], [1.98], [1.94], [1.98]])


previsoes_futuras = modelo_final.predict(novas_aberturas)
print('Previsões para os próximos 5 dias (04, 05, 06, 09, 10/06):')
for i, preco in enumerate(previsoes_futuras, start=1):
  print(f'Dia {i}: {preco:.2f}')