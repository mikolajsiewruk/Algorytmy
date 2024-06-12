from Dominik.lab10_Dominik import Graph
import pandas as pd

graph = Graph()
edges = [("A", "B", 8), ("B", "C", 6), ("C", "A", 7), ("B", "D", 5), ("E", "F", 2), ("F", "E", 2), ("G", "H", 3),
         ("H", "I", 4), ("I", "G", 2), ("C", "E", 2), ("F", "G", 3), ("D", "H", 4)]

for edge in edges:
    graph.add_edge(edge[0], edge[1], edge[2], 1)

print("Krawędzie grafu:", graph.display_edges())
print("macierz sąsiedztwa:")
matrix = graph.display_adjacency_matrix()
for row in matrix:
    print(row)

print("DFS od 0:", graph.dfs("A"))
print("BFS od 0:", graph.bfs("A"))

graph.draw_graph(1)

print("Silnie spójne składowe:", graph.kosaraju_scc())

data = {}
for i in range(len(matrix[0])):
    result = graph.dijkstra(matrix, 0, i)
    data.update({"Koniec: " + str(i): [result[0], result[1]]})

pd.set_option('display.expand_frame_repr', False)
df = pd.DataFrame(data, index=["Path", "Total length"])
print(df)