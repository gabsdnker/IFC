#Nome: Gabrielli Danker     Matéria: Estrutura de Dados II 

from collections import deque

class GrafoNaoDirigido:
    def __init__(self):
        self.vertices = {}  # Um dicionário onde as chaves são vértices e os valores são listas de vértices adjacentes.

    def insereV(self, v):
        if v not in self.vertices:
            self.vertices[v] = []

    def removeV(self, v):
        if v in self.vertices:
            for adjacente in self.vertices[v]:
                self.vertices[adjacente].remove(v)
            del self.vertices[v]

    def insereA(self, u, v):
        if u in self.vertices and v in self.vertices:
            if v not in self.vertices[u]:
                self.vertices[u].append(v)
            if u not in self.vertices[v]:
                self.vertices[v].append(u)

    def removeA(self, u, v):
        if u in self.vertices and v in self.vertices:
            if v in self.vertices[u]:
                self.vertices[u].remove(v)
            if u in self.vertices[v]:
                self.vertices[v].remove(u)

    def adj(self, v):
        return self.vertices[v]

    def getA(self, u, v):
        if u in self.vertices and v in self.vertices:
            if v in self.vertices[u]:
                return (u, v)
        return None

    def grau(self, v):
        return len(self.vertices[v])

    def verticesA(self, e):
        u, v = e
        return (u, v)

    def arestas(self):
        arestas = []
        for v, adjacentes in self.vertices.items():
            for adjacente in adjacentes:
                arestas.append((v, adjacente))
        return arestas

    def bfs(self, inicio):
        visitados = {}  # Dicionário para rastrear os vértices visitados
        fila = deque()  # Fila para BFS
        fila.append(inicio)  # Começamos a busca a partir do vértice inicial

        while fila:
            vertice = fila.popleft()
            if vertice not in visitados:
                visitados[vertice] = True
                print("Visitando:", vertice)

                # Enfileira todos os vizinhos não visitados
                for vizinho in self.adj(vertice):
                    if vizinho not in visitados:
                        fila.append(vizinho)

    def dfs(self, vertice, visitados=None):
        if visitados is None:
            visitados = {}  # Dicionário para rastrear os vértices visitados
        if vertice not in visitados:
            visitados[vertice] = True
            print("Visitando:", vertice)

            # Chama recursivamente a DFS nos vizinhos não visitados
            for vizinho in self.adj(vertice):
                if vizinho not in visitados:
                    self.dfs(vizinho, visitados)

    def __str__(self):
        result = "Vértices:\n"
        for vertex in self.vertices:
            result += f"{vertex}: {self.vertices[vertex]}\n"
        result += "Arestas:\n"
        for edge in self.arestas():
            result += f"{edge}\n"
        return result

    def isConexo(self):
        if not self.vertices:
            return True  # Um grafo vazio é considerado conexo

        visitados = set()
        fila = deque()
        primeiro_vertice = next(iter(self.vertices))

        fila.append(primeiro_vertice)
        visitados.add(primeiro_vertice)

        while fila:
            vertice = fila.popleft()

            for vizinho in self.adj(vertice):
                if vizinho not in visitados:
                    fila.append(vizinho)
                    visitados.add(vizinho)

        return len(visitados) == len(self.vertices)
    
def main():
    grafo = GrafoNaoDirigido()
    grafo.insereV('A')
    grafo.insereV('B')
    grafo.insereV('C')
    grafo.insereV('D')
    grafo.insereV('E')
    grafo.insereA('A', 'B')
    grafo.insereA('B', 'C')
    grafo.insereA('C', 'D')
    grafo.insereA('C', 'E')

    print("Ordem do grafo:", len(grafo.vertices))  # Saída: 5
    print("Tamanho do grafo:", len(grafo.arestas()))  # Saída: 6
    print("Vértices adjacentes a 'D':", grafo.adj('D'))  # Saída: ['C']
    print("Grau de 'D':", grafo.grau('D'))  # Saída: 1
    print("Arestas do grafo:", grafo.arestas())  # Saída: [('A', 'B'), ('B', 'A'), ('B', 'C'), ('C', 'B'), ('C', 'D'), ('C', 'E'), ('D', 'C'), ('E', 'C')]

    print("Busca em Largura:")
    grafo.bfs('A')

    print("Busca em Profundidade:")
    grafo.dfs('A')

    print("Conexidade do Grafo:", grafo.isConexo())  # Saída: True se o grafo for conexo
    
    print(grafo)  # Saída formatada do grafo

if __name__ == "__main__":
    main()

