#Nome: Gabrielli Danker      Matéria: Estrutura de Dados II

from collections import deque
import sys

class GrafoNaoDirigido:
    def __init__(self):
        self.vertices = {}
        self.vertice_para_indice = {}

    def insereV(self, v):
        if v not in self.vertices:
            self.vertices[v] = []
            self.vertice_para_indice[v] = len(self.vertices) - 1

    def insereA(self, u, v, w=float('inf')):
        if u in self.vertices and v in self.vertices:
            if v not in self.vertices[u]:
                self.vertices[u].append((v, w))
            if u not in self.vertices[v]:
                self.vertices[v].append((u, w))

    def floyd_warshall(self):
        V = len(self.vertices)
        dist = [[float('inf')] * V for _ in range(V)]

        for u in self.vertices:
            dist[self.vertice_para_indice[u]][self.vertice_para_indice[u]] = 0
            for v, w in self.vertices[u]:
                dist[self.vertice_para_indice[u]][self.vertice_para_indice[v]] = w

        for k in self.vertices:
            for i in self.vertices:
                for j in self.vertices:
                    if dist[self.vertice_para_indice[i]][self.vertice_para_indice[k]] + dist[self.vertice_para_indice[k]][self.vertice_para_indice[j]] < dist[self.vertice_para_indice[i]][self.vertice_para_indice[j]]:
                        dist[self.vertice_para_indice[i]][self.vertice_para_indice[j]] = dist[self.vertice_para_indice[i]][self.vertice_para_indice[k]] + dist[self.vertice_para_indice[k]][self.vertice_para_indice[j]]

        return dist

class GrafoPonderado:
    def __init__(self):
        self.vertices = {}
        self.arestas = []

    def insereV(self, v):
        if v not in self.vertices:
            self.vertices[v] = []

    def insereA(self, u, v, w):
        if u in self.vertices and v in self.vertices:
            if v not in self.vertices[u]:
                self.vertices[u].append((v, w))
            if u not in self.vertices[v]:
                self.vertices[v].append((u, w))
            self.arestas.append((u, v, w))

    def kruskal(self):
        result = []
        self.arestas.sort(key=lambda item: item[2])

        parent = {v: None for v in self.vertices}

        def find(x):
            if parent[x] is None:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y

        for u, v, w in self.arestas:
            if find(u) != find(v):
                result.append((u, v, w))
                union(u, v)

        return result

def main():
    grafo = GrafoNaoDirigido()
    grafo.insereV('A')
    grafo.insereV('B')
    grafo.insereV('C')
    grafo.insereA('A', 'B', 10)
    grafo.insereA('A', 'C', 6)
    grafo.insereA('B', 'C', 2)

    result_floyd = grafo.floyd_warshall()

    for row in result_floyd:
        print(row)

    grafo_ponderado = GrafoPonderado()
    grafo_ponderado.insereV('A')
    grafo_ponderado.insereV('B')
    grafo_ponderado.insereV('C')
    grafo_ponderado.insereA('A', 'B', 10)
    grafo_ponderado.insereA('A', 'C', 6)
    grafo_ponderado.insereA('B', 'C', 2)

    result_kruskal = grafo_ponderado.kruskal()

    for u, v, w in result_kruskal:
        print(f"Edge ({u}, {v}) with weight {w}")

if __name__ == "__main__":
    main()
