# Experiment 18: Alpha-Beta pruning
import math

leaf_values = [3, 5, 6, 9, 1, 2, 0, -1]
MAX_DEPTH = 3
visited = 0


def alphabeta(depth, node_index, is_max, values, alpha, beta):
    global visited
    if depth == MAX_DEPTH:
        visited += 1
        return values[node_index]

    if is_max:
        best = -math.inf
        for child in (node_index * 2, node_index * 2 + 1):
            best = max(best, alphabeta(depth + 1, child, False, values, alpha, beta))
            alpha = max(alpha, best)
            if beta <= alpha:
                print(f"  Pruned at MAX node (depth {depth}, index {node_index}): alpha={alpha}, beta={beta}")
                break
        return best
    else:
        best = math.inf
        for child in (node_index * 2, node_index * 2 + 1):
            best = min(best, alphabeta(depth + 1, child, True, values, alpha, beta))
            beta = min(beta, best)
            if beta <= alpha:
                print(f"  Pruned at MIN node (depth {depth}, index {node_index}): alpha={alpha}, beta={beta}")
                break
        return best


print("Leaf values:", leaf_values)
value = alphabeta(0, 0, True, leaf_values, -math.inf, math.inf)
print("\nOptimal value =", value)
print(f"Leaf nodes evaluated: {visited} of {len(leaf_values)}")
