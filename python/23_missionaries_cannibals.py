# Experiment 23: Missionaries and Cannibals (BFS)
# State = (missionaries_left, cannibals_left, boat) ; boat = 1 (left) / 0 (right)
from collections import deque

N = 3  # missionaries and cannibals
BOAT_MOVES = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]


def valid(m, c):
    if not (0 <= m <= N and 0 <= c <= N):
        return False
    if m != 0 and m < c:               # left bank
        return False
    mr, cr = N - m, N - c
    if mr != 0 and mr < cr:            # right bank
        return False
    return True


def solve():
    start, goal = (N, N, 1), (0, 0, 0)
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        (m, c, b), path = queue.popleft()
        if (m, c, b) == goal:
            return path
        for dm, dc in BOAT_MOVES:
            nm, nc = (m - dm, c - dc) if b == 1 else (m + dm, c + dc)
            state = (nm, nc, 1 - b)
            if valid(nm, nc) and state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))
    return None


path = solve()
print("State format: (Missionaries left, Cannibals left, Boat side)\n")
for i, (m, c, b) in enumerate(path):
    side = "Left " if b == 1 else "Right"
    print(f"Step {i:2d}: Left=({m}M,{c}C)  Right=({N-m}M,{N-c}C)  Boat on {side}")
print(f"\nSolved in {len(path) - 1} crossings.")
