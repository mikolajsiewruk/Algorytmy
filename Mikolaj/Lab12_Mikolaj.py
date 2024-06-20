import random as rnd
import time as tm
import numpy as np
import matplotlib.pyplot as plt
class Graph:
    def __init__(self):
        self.adjacency_matrix = []
        self.adjacency_list = {}


    def add_nodes(self,n):
        self.adjacency_matrix = [[0]*n for _ in range(n)]
        for i in range(n):
            self.adjacency_list[i] = []
        for i in range(n):
            available = [j for j in range(n) if j!=i]
            con_number = rnd.randint(1,n-1)
            nodes = rnd.choices(available,[1 for _ in range(len(available))], k = con_number)
            while nodes:
                node = rnd.choice(nodes)
                val = rnd.randint(1,50)
                if self.adjacency_matrix[i][node] == 0:
                    self.adjacency_matrix[i][node] = val
                    self.adjacency_matrix[node][i] = val
                    self.adjacency_list[i].append(node)
                    self.adjacency_list[node].append(i)
                elif val < self.adjacency_matrix[i][node] or val < self.adjacency_matrix[node][i]:
                    self.adjacency_matrix[i][node] = val
                    self.adjacency_matrix[node][i] = val
                    self.adjacency_list[i].append(node)
                    self.adjacency_list[node].append(i)
                nodes.remove(node)
    def convert(self):
        def helper(tup):
            return tup(2)
        vertices = []
        for i in range(len(self.adjacency_matrix)):
            for j in range(i,len(self.adjacency_matrix)):
                if self.adjacency_matrix[i][j]!= 0:
                    vertices.append((i,j,self.adjacency_matrix[i][j]))

        verts = sorted(vertices,key=lambda x:x[2])
        return verts

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
                e += 1
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

    def dijkstra(self,graph: list, start: int, end: int) -> tuple:
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
        counter = 0
        if start == end:
            print(start,end)
            print('aaaaaaa')
            return 1
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
            counter+=1
            if counter > 10000:
                print(start,end)
                print('xdxdxd')
                return -1
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
        return path, length, distances

g = Graph()
g.add_nodes(4)
print(g.adjacency_matrix)
dijkstra5, dijkstra10, dijkstra15, dijkstra20 = [], [], [], []
prim5, prim10, prim15, prim20 = [], [], [], []
ranges = [5,10,15,20]
krus = {}
prim = {}
dij = {}
for r in ranges:
    krus[r] = []
    prim[r] = []
    dij[r] = []
for i in range(100):
    for j in ranges:
        g = Graph()
        g.add_nodes(j)

        s1 = tm.perf_counter_ns()
        g.dijkstra(g.adjacency_matrix,rnd.randint(0,len(g.adjacency_matrix)-1),rnd.randint(0,len(g.adjacency_matrix)-1))
        e1 = tm.perf_counter_ns()
        dij[j].append(e1 - s1)

        s1 = tm.perf_counter_ns()
        g.Kruskal(g.adjacency_matrix,[i for i in range(-1)])
        e1 = tm.perf_counter_ns()
        krus[j].append(e1 - s1)

        s1 = tm.perf_counter_ns()
        g.Prim(g.adjacency_matrix, [i for i in range(j-1)])
        e1 = tm.perf_counter_ns()
        prim[j].append(e1 - s1)


print(krus,prim,dij)

kr = []
pr = []
dj = []
for r in ranges:
    kr.append(np.mean(krus[r]))
    pr.append(np.mean(prim[r]))
    dj.append(np.mean(dij[r]))


plt.plot(ranges,kr,label = "Kruskal")
plt.plot(ranges,pr,label = "Prim")
plt.plot(ranges,dj,label = "Dijkstra")
plt.legend()
plt.show()