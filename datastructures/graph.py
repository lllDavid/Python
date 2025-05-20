class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph:
            self.graph[vertex1].append(vertex2)
        else:
            self.graph[vertex1] = [vertex2]
    
    def get_neighbors(self, vertex):
        return self.graph.get(vertex, [])
    
    def __repr__(self):
        return str(self.graph)

g = Graph()

g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')

print(g)

print("Neighbors of A:", g.get_neighbors('A'))
print("Neighbors of B:", g.get_neighbors('B'))
print("Neighbors of C:", g.get_neighbors('C'))
