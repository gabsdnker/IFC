#pip install --break-system-packages pandas numpy matplotlib scikit-learn minisom

#obs.: Não esta mostrando a ideologia certa!! ARRUMAR

import pandas as pd
import numpy as np
from minisom import MiniSom
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D

# 1. Carregar matriz de votos
matriz = pd.read_csv(r'C:\Users\Blabl\OneDrive\Documentos\GitHub\IFC\IA\Projeto Final\CSVs\Votos 2024\matriz_votos_senadores.csv', index_col=0).fillna(0)

# 2. Carregar ideologia
ideologia_df = pd.read_csv(r'C:\Users\Blabl\OneDrive\Documentos\GitHub\IFC\IA\Projeto Final\CSVs\partidos\senadores_juntos.csv')
ideologia_df.set_index('Nome', inplace=True)

# 3. Alinhar dados
nomes_comuns = matriz.index.intersection(ideologia_df.index)
matriz = matriz.loc[nomes_comuns]
ideologia_df = ideologia_df.loc[nomes_comuns]
ideologia_df = ideologia_df.loc[matriz.index]

# 4. Treinar SOM
data = StandardScaler().fit_transform(matriz.values)
som_size = 15
som = MiniSom(x=som_size, y=som_size, input_len=data.shape[1], sigma=1.0, learning_rate=0.5, random_seed=42)
som.train_random(data, 2000)

# 5. Coordenadas dos neurônios vencedores
winner_coordinates = np.array([som.winner(x) for x in data])

# 6. Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(winner_coordinates)

# 7. Paletas de cores e formas
cores_clusters = ['red', 'green', 'blue']  # Cor da borda = cluster
ideologia_cores = {'Esquerda': 'purple', 'Centro': 'orange', 'Direita': 'cyan'}  # Cor de preenchimento
ideologia_marcadores = {'Esquerda': 'o', 'Centro': 's', 'Direita': '^'}  # Formato

# 8. Plotagem
fig, ax = plt.subplots(figsize=(14, 12))
ax.set_title('SOM - Senadores agrupados por voto\nCor = Ideologia | Borda = Cluster | Formato = Ideologia', fontsize=14)

# Fundo: U-Matrix
u_matrix = som.distance_map().T
ax.pcolor(u_matrix, cmap='coolwarm', alpha=0.6)

# Plot dos senadores
for i, (x, y) in enumerate(winner_coordinates):
    cluster_color = cores_clusters[clusters[i]]
    ideologia = ideologia_df.iloc[i, 0]
    ideologia_color = ideologia_cores.get(ideologia, 'gray')
    marcador = ideologia_marcadores.get(ideologia, 'x')
    
    ax.scatter(x + 0.5, y + 0.5, s=200, c=ideologia_color, marker=marcador,
               edgecolors=cluster_color, linewidths=2, alpha=0.95)
    ax.text(x + 0.5, y + 0.5, matriz.index[i], fontsize=8, ha='center', va='center',
            color='white', weight='bold')

# Legenda
legenda_clusters = [mpatches.Patch(color=cor, label=f'Cluster {i+1}') for i, cor in enumerate(cores_clusters)]
legenda_ideologias = [Line2D([0], [0], marker=ideologia_marcadores[ideol], color='w',
                             label=ideol, markerfacecolor=cor, markeredgecolor='black',
                             markersize=12, linewidth=0)
                      for ideol, cor in ideologia_cores.items()]
ax.legend(handles=legenda_clusters + legenda_ideologias, loc='center left', bbox_to_anchor=(1.02, 0.5), fontsize=10)

# Ajustes finais
ax.set_xlim(0, som_size)
ax.set_ylim(0, som_size)
ax.invert_yaxis()
ax.grid(False)
ax.set_xticks([])
ax.set_yticks([])

plt.tight_layout()
plt.show()

