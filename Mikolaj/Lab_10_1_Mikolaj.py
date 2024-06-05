import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)

    def remove_edge(self, u, v):
        if u in self.adj_list and v in self.adj_list[u]:
            self.adj_list[u].remove(v)
        if v in self.adj_list and u in self.adj_list[v]:
            self.adj_list[v].remove(u)

    def display_edges(self):
        edges = []
        for u in self.adj_list:
            for v in self.adj_list[u]:
                if (v, u) not in edges:
                    edges.append((u, v))
        return edges

    def adjacency_matrix(self):
        nodes = list(self.adj_list.keys())
        size = len(nodes)
        index_map = {nodes[i]: i for i in range(size)}
        adj_matrix = np.zeros((size, size), dtype=int)
        for u in self.adj_list:
            for v in self.adj_list[u]:
                adj_matrix[index_map[u]][index_map[v]] = 1
        return adj_matrix

    def incidence_matrix(self):
        nodes = list(self.adj_list.keys())
        edges = self.display_edges()
        size = len(nodes)
        num_edges = len(edges)
        index_map = {nodes[i]: i for i in range(size)}
        inc_matrix = np.zeros((size, num_edges), dtype=int)
        for edge_index, (u, v) in enumerate(edges):
            inc_matrix[index_map[u]][edge_index] = 1
            inc_matrix[index_map[v]][edge_index] = -1
        return inc_matrix

    def dfs(self, node, visited=None):
        if visited is None:
            visited = set()
        visited.add(node)
        result = [node]
        for neighbor in self.adj_list[node]:
            if neighbor not in visited:
                result.extend(self.dfs(neighbor, visited))
        return result

    def bfs(self, start_node):
        visited = set()
        queue = [start_node]
        result = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                result.append(node)
                queue.extend(self.adj_list[node])

        return result

    def display_graph(self):
        G = nx.DiGraph()
        for u in self.adj_list:
            for v in self.adj_list[u]:
                G.add_edge(u, v)

        pos = nx.spring_layout(G)
        plt.figure()
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, edge_color='gray')
        plt.show()
edges = [(0, 1), (0, 2), (1, 3), (3, 4), (2, 5), (6, 7), (3, 5), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
graph = Graph()

for u, v in edges:
    graph.add_edge(u, v)

# Wyświetlanie krawędzi grafu
print("Krawędzie grafu:", graph.display_edges())

# Wyświetlanie macierzy sąsiedztwa
print("Macierz sąsiedztwa:")
print(graph.adjacency_matrix())

# Wyświetlanie macierzy incydencji
print("Macierz incydencji:")
print(graph.incidence_matrix())

# Przeszukiwanie w głąb (DFS) za pomocą rekurencji
print("DFS (rekurencyjny) od wierzchołka 0:", graph.dfs(0))

# Przeszukiwanie wszerz (BFS)
print("BFS od wierzchołka 0:", graph.bfs(0))

graph.display_graph()