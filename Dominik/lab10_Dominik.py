import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, v1, v2, weight, parameter):
        if v1 not in self.adj_list:
            self.add_vertex(v1)
        if v2 not in self.adj_list:
            self.add_vertex(v2)
        if parameter == 1:  # directed graph
            self.adj_list[v1].append((v2, weight))
        elif parameter == 0:  # not directed graph
            self.adj_list[v1].append((v2, weight))
            self.adj_list[v2].append((v1, weight))

    def remove_vertex(self, v):
        if v in self.adj_list:
            for neighbor, _ in self.adj_list[v]:
                self.adj_list[neighbor] = [n for n in self.adj_list[neighbor] if n[0] != v]
            del self.adj_list[v]

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1] = [n for n in self.adj_list[v1] if n[0] != v2]
            self.adj_list[v2] = [n for n in self.adj_list[v2] if n[0] != v1]

    def display_edges(self):
        edges = []
        for v in self.adj_list:
            for neighbor, weight in self.adj_list[v]:
                if (neighbor, v, weight) not in edges:
                    edges.append((v, neighbor, weight))
        return edges

    def display_adjacency_matrix(self):
        vertices = list(self.adj_list.keys())
        matrix = [[0] * len(vertices) for _ in range(len(vertices))]
        for i, v in enumerate(vertices):
            for neighbor, weight in self.adj_list[v]:
                j = vertices.index(neighbor)
                matrix[i][j] = weight
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
                stack.extend(reversed([neighbor for neighbor, _ in self.adj_list[vertex]]))

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
                queue.extend([neighbor for neighbor, _ in self.adj_list[vertex]])

        return bfs_order

    def draw_graph(self, parameter):
        if parameter == 1:
            G = nx.DiGraph()  # Directed graph
        else:
            G = nx.Graph()  # Not directed graph
        for v in self.adj_list:
            for neighbor, weight in self.adj_list[v]:
                G.add_edge(v, neighbor, weight=weight)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=15, font_weight='bold')
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.show()

    def transpose(self):
        transposed_graph = Graph()
        for v in self.adj_list:
            for neighbor, weight in self.adj_list[v]:
                transposed_graph.add_edge(neighbor, v, weight, parameter=1)
        return transposed_graph

    def kosaraju_scc(self):
        stack = []
        visited = set()

        def fill_order(v):
            visited.add(v)
            for neighbor, _ in self.adj_list[v]:
                if neighbor not in visited:
                    fill_order(neighbor)
            stack.append(v)

        for v in self.adj_list:
            if v not in visited:
                fill_order(v)

        transposed_graph = self.transpose()
        visited.clear()
        scc = []

        def dfs(v, component):
            visited.add(v)
            component.append(v)
            for neighbor, _ in transposed_graph.adj_list[v]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        while stack:
            v = stack.pop()
            if v not in visited:
                component = []
                dfs(v, component)
                scc.append(component)

        return scc

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

