# Experiment 25: Breadth First Search (graph traversal)
from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}


def bfs(graph, start):
    visited = [start]
    queue = deque([start])
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for nb in graph[node]:
            if nb not in visited:
                visited.append(nb)
                queue.append(nb)


print("BFS traversal starting from A:")
bfs(graph, 'A')
print()
