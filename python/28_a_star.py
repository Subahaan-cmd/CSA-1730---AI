# Experiment 28: A* algorithm on a weighted graph
import heapq

graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('B', 2), ('C', 5), ('D', 12)],
    'B': [('C', 2)],
    'C': [('D', 3), ('G', 7)],
    'D': [('G', 2)],
    'G': [],
}
# Admissible heuristic h(n) = estimated cost from n to goal
h = {'S': 7, 'A': 6, 'B': 4, 'C': 4, 'D': 2, 'G': 0}


def a_star(start, goal):
    open_list = [(h[start], 0, start, [start])]    # (f, g, node, path)
    best_g = {start: 0}
    while open_list:
        f, g, node, path = heapq.heappop(open_list)
        if g > best_g.get(node, float('inf')):
            continue          # stale entry, a cheaper route was already found
        print(f"Expanding {node}: g={g}, h={h[node]}, f={f}")
        if node == goal:
            return path, g
        for nb, cost in graph[node]:
            new_g = g + cost
            if nb not in best_g or new_g < best_g[nb]:
                best_g[nb] = new_g
                heapq.heappush(open_list, (new_g + h[nb], new_g, nb, path + [nb]))
    return None, float('inf')


path, cost = a_star('S', 'G')
print("\nShortest path:", ' -> '.join(path))
print("Total cost   :", cost)
