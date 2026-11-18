# Experiment 30: 8 Puzzle Problem (A* with Manhattan distance)
import heapq

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)      # 0 = blank


def manhattan(state):
    d = 0
    for i, tile in enumerate(state):
        if tile:
            g = GOAL.index(tile)
            d += abs(i // 3 - g // 3) + abs(i % 3 - g % 3)
    return d


def neighbors(state):
    z = state.index(0)
    r, c = divmod(z, 3)
    for dr, dc, name in [(-1, 0, 'Up'), (1, 0, 'Down'), (0, -1, 'Left'), (0, 1, 'Right')]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            n = nr * 3 + nc
            s = list(state)
            s[z], s[n] = s[n], s[z]
            yield tuple(s), name


def solvable(state):
    t = [x for x in state if x]
    inv = sum(1 for i in range(len(t)) for j in range(i + 1, len(t)) if t[i] > t[j])
    return inv % 2 == 0


def solve(start):
    heap = [(manhattan(start), 0, start, [])]
    seen = {start: 0}
    while heap:
        f, g, state, moves = heapq.heappop(heap)
        if state == GOAL:
            return moves
        for nxt, mv in neighbors(state):
            if nxt not in seen or g + 1 < seen[nxt]:
                seen[nxt] = g + 1
                heapq.heappush(heap, (g + 1 + manhattan(nxt), g + 1, nxt, moves + [(mv, nxt)]))
    return None


def show(state):
    for i in range(0, 9, 3):
        print(' '.join(str(x) if x else '_' for x in state[i:i + 3]))
    print()


if __name__ == "__main__":
    start = (1, 2, 3,
             4, 0, 6,
             7, 5, 8)
    print("Start state:"); show(start)
    if not solvable(start):
        print("This puzzle is not solvable.")
    else:
        moves = solve(start)
        for i, (mv, st) in enumerate(moves, 1):
            print(f"Move {i}: {mv}"); show(st)
        print(f"Solved in {len(moves)} moves.")
