from Dominik.lab10_Dominik import Graph, StableMarriage

# Testing the graph with the provided edges
graph = Graph()
edges = [(0, 1, 1), (0, 2, 1), (1, 3, 1), (3, 4, 1), (2, 5, 1), (6, 7, 1), (3, 5, 1), (4, 5, 1), (5, 6, 1), (5, 7, 1), (6, 8, 1), (7, 8, 1), (8, 9, 1)]

for edge in edges:
    graph.add_edge(edge[0], edge[1], edge[2], 0)

print("Krawędzie grafu:", graph.display_edges())
print("Macierz sąsiedztwa:")
matrix = graph.display_adjacency_matrix()
for row in matrix:
    print(row)

print("DFS od A:", graph.dfs(0))
print("BFS od A:", graph.bfs(0))

graph.draw_graph(0)





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