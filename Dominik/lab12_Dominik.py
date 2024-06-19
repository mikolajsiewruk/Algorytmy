import random as rnd
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.matrix = {}

    def add_vertex(self, v):
        if v not in self.matrix:
            self.matrix[v] = []

    def remove_vertex(self, v):
        if v in self.matrix:
            for neighbor, _ in self.matrix[v]:
                self.matrix[neighbor] = [n for n in self.matrix[neighbor] if n[0] != v]
            del self.matrix[v]

    def add_edge(self, v1, v2, weight, parameter):
        if v1 not in self.matrix:
            self.add_vertex(v1)
        if v2 not in self.matrix:
            self.add_vertex(v2)
        if parameter == 1:  # directed graph
            self.matrix[v1].append((v2, weight))
        elif parameter == 0:  # not directed graph
            self.matrix[v1].append((v2, weight))
            self.matrix[v2].append((v1, weight))
        if not self.is_connected(v1):
            self.remove_vertex(v1)
            self.remove_vertex(v2)


    def dfs(self, start):
        visited = set()
        stack = [start]
        dfs_order = []

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                dfs_order.append(vertex)
                stack.extend(reversed([neighbor for neighbor, _ in self.matrix[vertex]]))

        return dfs_order

    def is_connected(self, vertice):
        if not self.matrix:
            return True
        visited_vertices = self.dfs(vertice)
        return len(visited_vertices) == len(self.matrix)

    def display_adjacency_matrix(self):
        vertices = list(self.matrix.keys())
        matrix = [[0] * len(vertices) for _ in range(len(vertices))]
        for i, v in enumerate(vertices):
            for neighbor, weight in self.matrix[v]:
                j = vertices.index(neighbor)
                matrix[i][j] = weight
        return matrix

    def generate_random_graph(self, num_vertices):
        while len(self.matrix) < num_vertices:
            a = rnd.randint(0, num_vertices-1)
            b = rnd.randint(0, num_vertices-1)
            if a != b:
                self.add_edge(a, b, rnd.randint(1, 50), 0)

        return self.display_adjacency_matrix()

    def draw_graph(self, parameter):
        if parameter == 1:
            G = nx.DiGraph()  # Directed graph
        else:
            G = nx.Graph()  # Not directed graph
        for v in self.matrix:
            for neighbor, weight in self.matrix[v]:
                print(v, neighbor)
                print(weight)
                G.add_edge(chr(v+65), chr(neighbor+65), weight=weight)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=15, font_weight='bold')
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.show()

    def Kruskal(self, new_graph: list, nodes: list) -> list:
        """
        Kruskal's algorithm for finding the edges in the Minimum Spanning Tree.
        :param new_graph: a graph of nodes in adjacency matrix form
        :param nodes: a list of nodes the Minimum Spanning Tree should contain
        :return: list of edges in the Minimum Spanning Tree
        """

        graph_list = []
        for i in range(len(new_graph)):
            for j in range(i, len(new_graph)):
                if new_graph[i][j] != 0:
                    graph_list.append([i, j, new_graph[i][j]])

        def find(parent: list, i: int) -> int:
            """
            Kruskal's algorithm helper function used for finding the root of a tree (checking if two nodes are in the same tree - preventing cycles)
            :param parent: list of parents of nodes in the tree
            :param i: index of the node in the tree
            :return: root of node
            """
            if parent[i] == i:
                return i
            return find(parent, parent[i])

        def union(parent: list, rank: list, x: int, y: int):
            """
            Kruskal's algorithm helper function used for uniting two disjoint sets, when adding an edge to MST
            :param parent: list of parents of nodes in the tree
            :param rank: list of tree heights for a given node
            :param x: index of the node in one tree
            :param y: index of the node in another tree
            """
            x_root = find(parent, x)
            y_root = find(parent, y)
            if rank[x_root] < rank[y_root]:
                parent[x_root] = y_root
            elif rank[x_root] > rank[y_root]:
                parent[y_root] = x_root
            else:
                parent[y_root] = x_root
                rank[x_root] += 1

        result = []
        i, e = 0, 0
        graph_list = sorted(graph_list, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(len(nodes)):
            parent.append(node)
            rank.append(0)
        while e < len(nodes) - 1:
            u, v, weight = graph_list[i]
            i += 1
            x = find(parent, u)
            y = find(parent, v)
            if x != y:
                e +=1
                result.append([u, v, weight])
                union(parent, rank, x, y)

        return result

    def Prim(self, new_graph: list, nodes: list) -> list:
        """
        Prim's algorithm for finding the edges in the Minimum Spanning Tree.
        :param new_graph: a graph of nodes in adjacency matrix form
        :param nodes: a list of nodes the Minimum Spanning Tree should contain
        :return: list of edges in the Minimum Spanning Tree
        """

        v_in_mst = set()
        v_not_in_mst = set((x for x in range(len(new_graph))))
        start = list(v_not_in_mst)[0]
        v_in_mst.add(start)
        v_not_in_mst.remove(start)
        edges = []
        while len(v_in_mst) < len(nodes):
            min = float('inf')
            for node_in_mst in v_in_mst:
                for node_not_in_mst in v_not_in_mst:
                    if new_graph[node_in_mst][node_not_in_mst] < min:
                        min = new_graph[node_in_mst][node_not_in_mst]
                        vertex = node_in_mst
                        closest = node_not_in_mst
            edges.append([vertex, closest])
            v_in_mst.add(closest)
            v_not_in_mst.remove(closest)

        return edges

    def dijkstra(self, graph: list, start: int, end: int) -> tuple:
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

g = Graph()
print(g.generate_random_graph(7))
g.draw_graph(0)