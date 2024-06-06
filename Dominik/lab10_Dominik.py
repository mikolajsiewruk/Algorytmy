import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, v1, v2):
        if v1 not in self.adj_list:
            self.add_vertex(v1)
        if v2 not in self.adj_list:
            self.add_vertex(v2)
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)

    def remove_vertex(self, v):
        if v in self.adj_list:
            for neighbor in self.adj_list[v]:
                self.adj_list[neighbor].remove(v)
            del self.adj_list[v]

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)

    def display_edges(self):
        edges = []
        for v in self.adj_list:
            for neighbor in self.adj_list[v]:
                if (neighbor, v) not in edges:
                    edges.append((v, neighbor))
        return edges

    def display_adjacency_matrix(self):
        vertices = list(self.adj_list.keys())
        matrix = [[0]*len(vertices) for _ in range(len(vertices))]
        for i, v in enumerate(vertices):
            for neighbor in self.adj_list[v]:
                j = vertices.index(neighbor)
                matrix[i][j] = 1
        return matrix

    def dfs(self, start):
        visited = set()
        stack = [start]
        dfs_order = []

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                dfs_order.append(vertex)
                stack.extend(reversed(self.adj_list[vertex]))

        return dfs_order

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        bfs_order = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                bfs_order.append(vertex)
                queue.extend(self.adj_list[vertex])

        return bfs_order

    def draw_graph(self):
        G = nx.Graph()
        for v in self.adj_list:
            for neighbor in self.adj_list[v]:
                G.add_edge(v, neighbor)
        nx.draw(G, with_labels=True, node_color='lightblue', node_size=700, font_size=15, font_weight='bold')
        plt.show()


class StableMarriage:
    def __init__(self, men_preferences, women_preferences):
        self.men_preferences = men_preferences
        self.women_preferences = women_preferences
        self.n = len(men_preferences)
        self.free_men = list(men_preferences.keys())
        self.engaged = {}

    def match(self):
        while self.free_men:
            man = self.free_men[0]
            man_pref_list = self.men_preferences[man]
            for woman in man_pref_list:
                if woman not in self.engaged:
                    self.engaged[woman] = man
                    self.free_men.remove(man)
                    break
                else:
                    current_man = self.engaged[woman]
                    woman_pref_list = self.women_preferences[woman]
                    if woman_pref_list.index(man) < woman_pref_list.index(current_man):
                        self.engaged[woman] = man
                        self.free_men.remove(man)
                        self.free_men.append(current_man)
                        break
        return self.engaged

# Testing the graph with the provided edges
graph = Graph()
edges = [(0, 1), (0, 2), (1, 3), (3, 4), (2, 5), (6, 7), (3, 5), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for edge in edges:
    graph.add_edge(*edge)

print("Krawędzie grafu:", graph.display_edges())
print("macierz sąsiedztwa:")
matrix = graph.display_adjacency_matrix()
for row in matrix:
    print(row)

print("DFS od 0:", graph.dfs(9))
print("BFS od 0:", graph.bfs(0))

graph.draw_graph()





# Example usage:
men_preferences = {
    'A': ['X', 'Y', 'Z'],
    'B': ['Y', 'X', 'Z'],
    'C': ['X', 'Y', 'Z']
}

women_preferences = {
    'X': ['B', 'A', 'C'],
    'Y': ['A', 'C', 'B'],
    'Z': ['A', 'B', 'C']
}

stable_marriage = StableMarriage(men_preferences, women_preferences)
matches = stable_marriage.match()
print("Stable marriages:", matches)
