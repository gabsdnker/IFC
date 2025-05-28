# pip install minisom --break-system-packages

#ESTÁ DANDO ERRO
import pandas as pd
import numpy as np
from minisom import MiniSom
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# 1. Carregar matriz votos
matriz = pd.read_csv('CSVs/Votos 2024/matriz_votos_senadores.csv', index_col=0)
matriz = matriz.fillna(0)

# 2. Carregar ideologia
ideologia_df = pd.read_csv('CSVs/partidos/senadores_juntos.csv')
ideologia_df.set_index('Nome', inplace=True)

# Garantir ordem igual
ideologia_df = ideologia_df.loc[matriz.index]

# 3. Dados para o SOM
data = matriz.values
scaler = StandardScaler()
data_norm = scaler.fit_transform(data)

# 4. Treinar SOM
som_size = 15
som = MiniSom(x=som_size, y=som_size, input_len=data_norm.shape[1], sigma=1.0, learning_rate=0.5, random_seed=42)
som.train_random(data_norm, 2000)

# 5. Neurônios vencedores
winner_coordinates = np.array([som.winner(x) for x in data_norm])

# 6. Clustering nos neurônios
k = 3
kmeans = KMeans(n_clusters=k, random_state=42)
clusters = kmeans.fit_predict(winner_coordinates)

# 7. Cores clusters e ideologias
cores_clusters = ['red', 'green', 'blue']
ideologia_cores = {'esquerda': 'purple', 'centro': 'orange', 'direita': 'cyan'}

# 8. Plotagem
plt.figure(figsize=(10, 10))
plt.title('SOM - Senadores agrupados por voto\nCores = Clusters SOM | Bordas = Ideologia')

# U-Matrix
plt.pcolor(som.distance_map().T, cmap='coolwarm', alpha=0.6)

for i, (x, y) in enumerate(winner_coordinates):
    cluster_color = cores_clusters[clusters[i]]
    ideologia_color = ideologia_cores.get(ideologia_df.iloc[i, 0], 'black')
    plt.scatter(x + 0.5, y + 0.5, marker='o', s=150, color=cluster_color,
                edgecolor=ideologia_color, linewidth=2, alpha=0.8)
    plt.text(x + 0.5, y + 0.5, matriz.index[i], fontsize=7, ha='center', va='center')

legendas = [mpatches.Patch(color=cor, label=f'Cluster {i+1}') for i, cor in enumerate(cores_clusters)]
for ideol, cor in ideologia_cores.items():
    legendas.append(plt.Line2D([0], [0], marker='o', color='w', label=ideol,
                              markerfacecolor='w', markeredgecolor=cor, markersize=10, linewidth=2))
plt.legend(handles=legendas, loc='upper right')

plt.grid(False)
plt.show()
