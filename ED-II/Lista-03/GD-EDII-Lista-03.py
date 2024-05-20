#Nome: Gabrielli Danker      Matéria: Estrutura de Dados II

# Algoritmo de Floyd

def floyd_warshall(graph):
    # Inicialização
    V = len(graph)
    dist = [[float('inf')] * V for _ in range(V)]  # Inicializa uma matriz de distâncias com infinito
    for i in range(V):
        dist[i][i] = 0  # Define a distância de um vértice para ele mesmo como 0
    for u in range(V):
        for v in range(V):
            dist[u][v] = graph[u][v]  # Inicializa a matriz de distâncias com os valores diretos do grafo

    # Loop Principal
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]  # Atualiza a distância se um caminho menor for encontrado

    return dist  # Retorna a matriz de distâncias mínimas entre todos os pares de vértices

# Exemplo de uso
graph = [
    [0, 3, float('inf'), 7],
    [8, 0, 2, float('inf')],
    [5, float('inf'), 0, 1],
    [2, float('inf'), float('inf'), 0]
]

result = floyd_warshall(graph)  # Chama o algoritmo de Floyd-Warshall com o grafo de exemplo
for row in result:
    print(row)  # Imprime a matriz de distâncias mínimas entre todos os pares de vértices

#[0, 3, 5, 6]
#[5, 0, 2, 3]
#[3, 6, 0, 1]
#[2, 5, 7, 0]