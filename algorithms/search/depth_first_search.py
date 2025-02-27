graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  
    
    visited.add(start)
    print(start, end=" ")  

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

dfs(graph, 0)
