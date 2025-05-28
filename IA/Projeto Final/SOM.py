import pandas as pd
import numpy as np
from minisom import MiniSom  # Biblioteca para SOM
import matplotlib.pyplot as plt

# 1. Ler CSV com nomes, partidos e posição
df_senadores = pd.read_csv('CSVs/partidos/senadores_juntos.csv')  # Nome, Partido, Posição (Esq, Dir, Centro)

# 2. Ler CSV com votos nominais de 2024 (exemplo para um arquivo)
df_votos = pd.read_csv('CSVs/votos_2024.csv')  
# Supondo que df_votos tem colunas: 'Nome', 'Voto1', 'Voto2', ..., 'VotoN'

# 3. Unir as tabelas pelo Nome
df = pd.merge(df_senadores, df_votos, on='Nome')

# 4. Converter votos para matriz numérica
def map_voto(voto):
    if voto in ['Sim', 'AV', 'Votou', 'A Favor']:  # Exemplo de votos afirmativos
        return 1
    elif voto == 'Não':
        return -1
    else:
        return 0  # Ausência, abstenção, etc.

voto_cols = [col for col in df.columns if col.startswith('Voto')]
for col in voto_cols:
    df[col] = df[col].apply(map_voto)

X = df[voto_cols].values  # Matriz de votos numérica

# 5. Treinar SOM
som = MiniSom(x=10, y=10, input_len=X.shape[1], sigma=1.0, learning_rate=0.5)
som.random_weights_init(X)
som.train_random(X, 1000)  # Treina SOM por 1000 iterações

# 6. Visualizar o SOM
plt.figure(figsize=(10,10))
wmap = {}

for i, x in enumerate(X):
    w = som.winner(x)
    wmap.setdefault(w, []).append(i)

# Plotando cada senador com cor pela posição política
colors = {'Esquerda': 'red', 'Direita': 'blue', 'Centro': 'green'}

for position, color in colors.items():
    indices = df[df['Posição'] == position].index
    for i in indices:
        w = som.winner(X[i])
        plt.plot(w[0]+.5, w[1]+.5, 'o', markerfacecolor=color, markeredgecolor='k', markersize=12)

plt.title('Mapa SOM dos Senadores (por posição política)')
plt.grid()
plt.show()
