# Experiment 29: Breadth First Search - shortest path in a graph and level-order view
from collections import deque

graph = {
    'S': ['A', 'B'],
    'A': ['S', 'C', 'D'],
    'B': ['S', 'E'],
    'C': ['A', 'G'],
    'D': ['A', 'G'],
    'E': ['B', 'G'],
    'G': ['C', 'D', 'E'],
}


def bfs_shortest_path(graph, start, goal):
    queue = deque([[start]])
    visited = {start}
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        for nb in graph[node]:
            if nb not in visited:
                visited.add(nb)
                queue.append(path + [nb])
    return None


def bfs_levels(graph, start):
    levels, visited, frontier = [], {start}, [start]
    while frontier:
        levels.append(frontier)
        nxt = []
        for node in frontier:
            for nb in graph[node]:
                if nb not in visited:
                    visited.add(nb)
                    nxt.append(nb)
        frontier = nxt
    return levels


print("Levels from S:")
for i, lvl in enumerate(bfs_levels(graph, 'S')):
    print(f"  Level {i}: {lvl}")

p = bfs_shortest_path(graph, 'S', 'G')
print("\nShortest path S -> G:", ' -> '.join(p), f"(length {len(p) - 1})")
