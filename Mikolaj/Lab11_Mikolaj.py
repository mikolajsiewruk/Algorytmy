import networkx as nx
import matplotlib.pyplot as plt
from Lab_10_1_Mikolaj import Graph

class DiGraph(Graph):
    def __init__(self):
        self.adj_list1 = {}
        self.adj_list ={}
        self.stack = []
        self.edges = []
    def display_graph(self):
        G = nx.DiGraph()
        for u in self.adj_list:
            for nodes in self.adj_list[u]:
                G.add_edge(u,nodes[0],weight=nodes[1])
        elarge = [(u, v) for (u, v, d) in G.edges(data=True)]
        pos = nx.spring_layout(G,seed = 7)
        plt.figure()
        nx.draw_networkx_nodes(G, pos, node_size=400)
        nx.draw_networkx_edges(G, pos, edgelist=elarge, width=3)
        nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels)
        plt.show()

    def add_edge(self, u, v,weight):
        if u not in self.adj_list:
            self.adj_list[u] = []
            self.adj_list1[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
            self.adj_list1[v] = []
        self.adj_list[u].append((v,weight))
        self.edges.append((u,v,weight))
        self.adj_list1[u].append(v)
    def dfs(self,v, visited, stack):
        visited.add(v)
        print('s',stack)
        print('v',visited)
        print(self.adj_list1[v])
        for neighbour in self.adj_list1[v]:
            print('n',neighbour)
            if neighbour not in visited:
                print('yes')
                self.dfs(neighbour, visited, stack)

            else:
                print('no')
        print('val', v)
        stack.append(v)

        return stack

    def adjacency_matrix(self):
        nodes = list(self.adj_list.keys())
        size = len(nodes)
        index_map = {nodes[i]: i for i in range(size)}
        adj_matrix = [[0]*len(self.adj_list) for _ in range(len(self.adj_list))]
        for u in self.adj_list:
            for v in self.adj_list[u]:
                adj_matrix[u][v[0]] = v[1]
        return adj_matrix
    def korosaju(self):
        print('xd',self.adj_list1)
        def reverse_graph(graph):
            reversed = DiGraph()
            for u,v,weight in graph:
                reversed.add_edge(v,u,weight)
            return reversed

        ssc = []
        visited = set()
        nodes = [edge[0] for edge in self.edges]
        for node in nodes:
            if node not in visited:
                self.dfs(node,set(),self.stack)
                print('stack',node,self.stack)
                rev = reverse_graph(self.edges)
                unvisited = [edge[0] for edge in self.edges]
                print(self.stack)
                while self.stack:
                    node = self.stack.pop()
                    if node not in visited:
                        ssc.append(rev.dfs(node,visited,[]))

        return ssc




graph = DiGraph()
edges = [
    (0, 1, 8),
    (1, 2, 6),
    (2, 0, 7),
    (1, 3, 5),
    (4, 5, 2),
    (5, 4, 2),
    (6, 7, 3),
    (7, 8, 4),
    (8, 6, 2),
    (2, 4, 2),
    (5, 6, 3),
    (3, 7, 4),
]

for u, v, weight in edges:
    graph.add_edge(u, v, weight)

print(graph.adj_list)
graph.display_graph()
print(graph.korosaju())


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
        if graph[j].count(0) != 0:
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
    return path, length,distances

a = graph.adjacency_matrix()
print(a)

print(dijkstra(a,1,7))