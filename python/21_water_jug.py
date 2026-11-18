# Experiment 21: Water Jug Problem (BFS over states)
from collections import deque


def water_jug(cap_a, cap_b, target):
    start = (0, 0)
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        (a, b), path = queue.popleft()
        if a == target or b == target:
            return path
        pour_ab = min(a, cap_b - b)
        pour_ba = min(b, cap_a - a)
        moves = [
            (cap_a, b), (a, cap_b),            # fill A / fill B
            (0, b), (a, 0),                    # empty A / empty B
            (a - pour_ab, b + pour_ab),        # pour A -> B
            (a + pour_ba, b - pour_ba),        # pour B -> A
        ]
        for state in moves:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))
    return None


if __name__ == "__main__":
    jug_a, jug_b, goal = 4, 3, 2
    solution = water_jug(jug_a, jug_b, goal)
    if solution:
        print(f"Jugs: {jug_a}L and {jug_b}L, target: {goal}L")
        print("Steps (A, B):")
        for i, s in enumerate(solution):
            print(f"  Step {i}: {s}")
    else:
        print("No solution possible")
