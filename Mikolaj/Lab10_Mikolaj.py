class Graph:
    def __init__(self):
        self.nodes = []
        self.connections = []
        self.adjacency_matrix = []

    def add_edge(self,u,v):
        self.connections.append((u,v))

    def remove_edge(self,u,v):
        self.connections.remove((u,v))

    def show_adjacency_matrix(self):
        for i in range(len(self.connections)):
            m = max(self.connections[i])
        self.adjacency_matrix = [[0]*(m+1) for _ in range(m+1)]

        for connection in self.connections:
            print(connection)
            self.adjacency_matrix[connection[0]][connection[1]]= 1
            self.adjacency_matrix[connection[1]][connection[0]] = 1


        print(self.adjacency_matrix)
g = Graph()
g.add_edge(0,1)
g.add_edge(5,6)
g.show_adjacency_matrix()