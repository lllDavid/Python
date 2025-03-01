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
