import sys
import networkx as nx
import matplotlib.pyplot as plt
 
class Graph():
 
    def __init__(self, vertx):
        self.V = vertx
        # Creando una matriz para representar el grafo, inicialmente se inicializa con 0's.
        self.graph = [[0 for column in range(vertx)]
                      for row in range(vertx)]
        
        self.p = []
 
    def pSol(self, dist):
        # Imprimiendo la distancia de cada nodo al nodo origen.
        print("Distancia de cada nodo desde el origen")
        for node in range(self.V):
            print(node, "t", dist[node])
 

    def minDistance(self, dist, sptSet):
 
        # Encontramos el vértice con la distancia mínima del conjunto de vértices aún no procesados
        min = sys.maxsize
 

        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index
 

    def dijk(self, source):
        # Inicializamos las distancias a cada nodo con infinito excepto el nodo de origen, y marcamos todos los nodos como no procesados
        dist = [sys.maxsize] * self.V
        dist[source] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
 
            u = self.minDistance(dist, sptSet)
 
            sptSet[u] = True
 

            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                   dist[v] = dist[u] + self.graph[u][v]
                   self.p.append(v)
        
        # Imprimimos las distancias
        self.pSol(dist)

# Creamos una instancia de la clase Graph con 9 vértices
f = Graph(9) 

# Definimos el grafo con una matriz de adyacencia
f.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

# Creando el un objeto Graph de newtworkx.
G = nx.Graph()

# Añadiendo los nodos al grafo.
for i in range(f.V):
    G.add_node(i)

# Añadiendo las aristas al grafo.
# Añadimos las aristas al grafo
for i in range(f.V):
    for j in range(i+1, f.V):
        if f.graph[i][j] > 0:
            G.add_edge(i, j, weight=f.graph[i][j])

# Ejecutamos el algoritmo de Dijkstra para encontrar la ruta más corta desde el nodo 0 
f.dijk(0)

# Obtenemos los nodos y las aristas de la ruta más corta
path_nodes = []
path_edges = []
for i in range(1, len(f.p) - 1):
    path_nodes.append(f.p[i])
    path_edges.append((f.p[i], f.p[i+1]))

# Graficamos el grafo y resaltamos la ruta más corta
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue')
nx.draw_networkx_edges(G, pos, width=1, edge_color='gray')
nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=2, edge_color='red')
nx.draw_networkx_labels(G, pos, font_size=14, font_family='sans-serif')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(i, j): f.graph[i][j] for i in range(9) for j in range(i+1, 9) if f.graph[i][j] > 0})
plt.axis('off')
plt.show()