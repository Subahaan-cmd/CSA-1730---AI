# Experiment 26: Depth First Search (recursive and iterative)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}


def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = []
    visited.append(node)
    for nb in graph[node]:
        if nb not in visited:
            dfs_recursive(graph, nb, visited)
    return visited


def dfs_iterative(graph, start):
    visited, stack = [], [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))
    return visited


print("DFS (recursive):", dfs_recursive(graph, 'A'))
print("DFS (iterative):", dfs_iterative(graph, 'A'))
