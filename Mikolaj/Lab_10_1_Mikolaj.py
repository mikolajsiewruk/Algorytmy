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
        adj_matrix = [[0]*10 for _ in range(len(self.adj_list))]
        for u in self.adj_list:
            for v in self.adj_list[u]:
                adj_matrix[u][v] = 1
                adj_matrix[v][u] = 1
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
        G = nx.Graph()
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
print(a:=graph.adjacency_matrix())
print(graph.adj_list)

# Wyświetlanie macierzy incydencji
print("Macierz incydencji:")
print(graph.incidence_matrix())

# Przeszukiwanie w głąb (DFS) za pomocą rekurencji
print("DFS od wierzchołka 0:", graph.dfs(0))

# Przeszukiwanie wszerz (BFS)
print("BFS od wierzchołka 0:", graph.bfs(0))

graph.display_graph()

def dijkstra(graph: list, start: int, end: int) -> tuple:
    """
    Dijkstra's algorithm for finding the shortest path in a graph.
    :param graph: a graph of nodes in adjacency matrix form
    :param start: source
    :param end: target
    :return: list of shortest distances from node 0 to the last node
    """

    # noinspection PyTypeChecker
    def reconstruct(distances: list, start: int, end: int) -> list:
        """
        Dijkstra helper function. From a given list of shortest connections returns full path.
        :param distances: List of dictionaries containing node number ("node") and list of [from which node,total distance] ("val")
        :param start: source
        :param end: target
        :return: reconstructed path
        """
        path = []
        curr = distances[end]  # set the pointer at the last node of the path
        while str(curr["val"][
                      0]) != '':  # from the last node add the values of "val"[0] key that keep track of the shortest path available.
            path.append(curr["node"])
            curr = distances[curr["val"][0]]
        path.append(start)
        path.reverse()
        return path

    unvisited = set()  # set containing all unvisited nodes
    reachable = [x for x in graph if x.count(0) < len(graph)]  # temporary fix
    visited = []
    for j in range(len(graph)):
        unvisited.add(j)
    distances = []
    for i in range(len(graph)):
        if i == start:
            distances.append({"node": i, "val": ['', 0]})
        else:
            distances.append({"node": i, "val": ['',
                                                 'inf']})  # every node as a dictionary with "val" being an array [from which node,total distance]
    current = start
    prev = []
    while unvisited:  # searching process will continue until it checks all the nodes
        if current not in prev:
            prev.append(current)
        neighbors = [i for i in range(len(graph[current])) if (graph[current][i] != 0 and i in unvisited)]
        for node in neighbors:  # consider all neighboring nodes
            dist = distances[node]["val"][1]
            new_dist = distances[current]["val"][1] + graph[current][
                node]  # calculate the distance from the current node to each neighbor
            if dist == 'inf' or new_dist < dist:  # if the new path is shorter, switch
                distances[node]["val"][1] = new_dist
                distances[node]["val"][0] = current
        unvisited.remove(current)  # remove current node from unvisited
        if current not in visited:
            visited.append(current)
        valid = [nodes for nodes in distances if nodes["val"][1] != 'inf' and nodes[
            "node"] in unvisited]  # consider all nodes that connect to current node and are not yet visited
        v = [nodes["val"][1] for nodes in distances if
             nodes["val"][1] != 'inf' and nodes["node"] in unvisited]  # take their path distances
        if not valid:
            current = visited[visited.index(current) - 1]
            unvisited.add(current)
        if not valid and len(visited) == len(reachable):
            break

        for nodes in valid:  # from path distances select the one with the shortest distance
            if nodes["val"][1] == min(v):
                current = nodes["node"]
    path = reconstruct(distances, start, end)
    length = distances[end]["val"][1]
    return path, length

print(dijkstra(list(a),1,2))