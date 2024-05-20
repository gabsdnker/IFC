#Nome: Gabrielli Danker      Matéria: Estrutura de Dados II

# Algoritmo de Kruskal

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def kruskal(self):
        result = []
        self.graph = sorted(self.graph, key=lambda item: item[2])  # Ordena as arestas por peso
        parent = [i for i in range(self.V)]  # Inicializa uma lista de pais para cada vértice

        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            parent[root_x] = root_y

        for i in range(len(self.graph)):
            u, v, w = self.graph[i]
            if find(u) != find(v):  # Verifica se adicionar a aresta não forma um ciclo
                result.append([u, v, w])  # Adiciona a aresta ao resultado
                union(u, v)  # Une os conjuntos dos vértices conectados pela aresta

        return result  # Retorna a lista de arestas na árvore geradora mínima

# Exemplo de uso
g = Graph(4)  # Cria um grafo com 4 vértices
g.add_edge(0, 1, 10)  # Adiciona aresta entre vértices 0 e 1 com peso 10
g.add_edge(0, 2, 6)   # Adiciona aresta entre vértices 0 e 2 com peso 6
g.add_edge(0, 3, 5)   # Adiciona aresta entre vértices 0 e 3 com peso 5
g.add_edge(1, 3, 15)  # Adiciona aresta entre vértices 1 e 3 com peso 15
g.add_edge(2, 3, 4)   # Adiciona aresta entre vértices 2 e 3 com peso 4

result = g.kruskal()  # Chama o algoritmo de Kruskal para encontrar a árvore geradora mínima
for u, v, w in result:
    print(f"Edge ({u}, {v}) with weight {w}")  # Imprime as arestas na árvore geradora mínima

#Edge (2, 3) with weight 4
#Edge (0, 3) with weight 5
#Edge (0, 1) with weight 10