# pip install --break-system-packages pandas numpy matplotlib scikit-learn minisom
import pandas as pd
import numpy as np
from minisom import MiniSom
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
import os

# Criar pasta de saída
os.makedirs('../imagens', exist_ok=True)

# 1. Carregar matriz de votos
matriz = pd.read_csv(
    '../CSVs/Votos 2024/matriz_votos_senadores.csv',
    index_col=0
).fillna(0)

# 2. Carregar ideologia
ideologia_df = pd.read_csv(
    '../CSVs/partidos/senadores_juntos.csv'
)
ideologia_df.set_index('Nome', inplace=True)

# 3. Alinhar dados
nomes_comuns = matriz.index.intersection(ideologia_df.index)
matriz = matriz.loc[nomes_comuns]
ideologia_df = ideologia_df.loc[nomes_comuns]

# 4. Normalizar os dados
data = StandardScaler().fit_transform(matriz.values)

# 5. Treinar SOM
som_size = 15
som = MiniSom(x=som_size, y=som_size, input_len=data.shape[1],
              sigma=1.0, learning_rate=0.5, random_seed=42)
som.train_random(data, 2000)

# 6. Coordenadas dos neurônios vencedores
winner_coordinates = np.array([som.winner(x) for x in data])

# 7. Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(winner_coordinates)

# 8. Cores e formatos
cores_clusters = ['red', 'green', 'blue']  # Borda = cluster
ideologia_cores = {'Esquerda': 'purple', 'Centro': 'orange', 'Direita': 'cyan'}
ideologia_marcadores = {'Esquerda': 'o', 'Centro': 's', 'Direita': '^'}

# 9. Plotagem
fig, ax = plt.subplots(figsize=(14, 12), facecolor='white')
ax.set_title('🧠 SOM - Agrupamento de Senadores por Votação',
             fontsize=16, fontweight='bold', color='darkblue')

# Fundo com U-Matrix
u_matrix = som.distance_map().T
ax.pcolor(u_matrix, cmap='coolwarm', alpha=0.6)

# Plotar senadores
for i, (x, y) in enumerate(winner_coordinates):
    nome = matriz.index[i]
    ideologia = ideologia_df.loc[nome, 'Posição']
    cluster_color = cores_clusters[clusters[i]]
    ideologia_color = ideologia_cores.get(ideologia, 'gray')
    marcador = ideologia_marcadores.get(ideologia, 'x')

    ax.scatter(x + 0.5, y + 0.5, s=220, c=ideologia_color, marker=marcador,
               edgecolors=cluster_color, linewidths=2, alpha=0.95)
    ax.text(x + 0.5, y + 0.5, nome.split()[0], fontsize=7.5,
            ha='center', va='center', color='white', weight='bold')

# Legenda
legenda_clusters = [mpatches.Patch(color=cor, label=f'Cluster {i+1}')
                    for i, cor in enumerate(cores_clusters)]

legenda_ideologias = [
    Line2D([0], [0], marker=ideologia_marcadores[ideol], color='w',
           label=ideol, markerfacecolor=cor, markeredgecolor='black',
           markersize=12, linewidth=0)
    for ideol, cor in ideologia_cores.items()
]

ax.legend(handles=legenda_clusters + legenda_ideologias,
          loc='center left', bbox_to_anchor=(1.02, 0.5), fontsize=10)

# Ajustes finais
ax.set_xlim(0, som_size)
ax.set_ylim(0, som_size)
ax.invert_yaxis()
ax.grid(False)
ax.set_xticks([])
ax.set_yticks([])

# Salvar e mostrar
plt.tight_layout()
plt.savefig('../imagens/som_senadores.png', dpi=300, facecolor='white')
plt.show()