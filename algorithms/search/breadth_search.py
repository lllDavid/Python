from collections import deque

def bfs(graph, start):
    visited = set()  
    queue = deque([start])
    visited.add(start)  

    while queue:
        node = queue.popleft()
        print(node, end=' ')  

        for neighbor in graph[node]:  
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)  

graph1 = {  
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F', 'G'},
    'D': {'B'},
    'E': {'B', 'H'},
    'F': {'C'},
    'G': {'C'},
    'H': {'E'}
}

graph2 = {  
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

print("graph1:")
bfs(graph1, 'A')

print("\ngraph2:")
bfs(graph2, '5')
