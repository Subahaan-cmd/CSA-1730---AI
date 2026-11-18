# Experiment 17: Minimax algorithm
# Game tree: depth 3, binary branching. Leaves hold utility values.
# MAX moves at the root.

leaf_values = [3, 5, 6, 9, 1, 2, 0, -1]
MAX_DEPTH = 3


def minimax(depth, node_index, is_max, values, path):
    if depth == MAX_DEPTH:
        return values[node_index]
    left = minimax(depth + 1, node_index * 2, not is_max, values, path)
    right = minimax(depth + 1, node_index * 2 + 1, not is_max, values, path)
    best = max(left, right) if is_max else min(left, right)
    print(f"{'MAX' if is_max else 'MIN'} node at depth {depth}, index {node_index}: "
          f"children=({left}, {right}) -> {best}")
    return best


print("Leaf values:", leaf_values)
print()
result = minimax(0, 0, True, leaf_values, [])
print("\nOptimal value for MAX at the root =", result)
