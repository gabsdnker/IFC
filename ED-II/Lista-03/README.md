## Algoritmo de Floyd

- O algoritmo de Floyd-Warshall é implementado para encontrar as distâncias mínimas entre todos os pares de vértices em um grafo ponderado.

- A matriz dist é inicializada com valores infinitos, exceto nas posições da diagonal principal, onde as distâncias de um vértice para ele mesmo são definidas como 0.

- Em seguida, o loop principal é usado para iterar sobre todos os vértices e encontrar as distâncias mínimas.

- Se uma distância menor for encontrada passando por um vértice intermediário (k), a matriz de distâncias é atualizada.

- O resultado final é uma matriz que contém as distâncias mínimas entre todos os pares de vértices.

## Algoritmo de Kruskal

- É implementado o Algoritmo de Kruskal para encontrar a árvore geradora mínima em um grafo ponderado.
  
- A classe Graph é usada para representar o grafo e implementa métodos para adicionar arestas e executar o algoritmo de Kruskal.
  
- As arestas do grafo são adicionadas usando o método add_edge, que recebe os vértices de origem e destino e o peso da aresta.
  
- O método kruskal ordena as arestas por peso e, em seguida, executa o algoritmo de Kruskal para encontrar a árvore geradora mínima.
  
- As funções find e union são usadas para verificar se adicionar uma aresta forma um ciclo no grafo e, se não, para uni-los na mesma árvore.
  
- O resultado final é uma lista de arestas na árvore geradora mínima, que é impressa no final do código.
