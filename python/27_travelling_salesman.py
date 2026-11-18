# Experiment 27: Travelling Salesman Problem (brute force + nearest-neighbour heuristic)
from itertools import permutations

cities = ['A', 'B', 'C', 'D']
dist = {
    'A': {'A': 0,  'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0,  'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0,  'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0},
}


def tour_cost(tour):
    return sum(dist[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))


def tsp_brute_force(start):
    others = [c for c in cities if c != start]
    best_cost, best_tour = float('inf'), None
    for perm in permutations(others):
        tour = [start] + list(perm) + [start]
        cost = tour_cost(tour)
        print(f"  {' -> '.join(tour)}  cost = {cost}")
        if cost < best_cost:
            best_cost, best_tour = cost, tour
    return best_tour, best_cost


def nearest_neighbour(start):
    tour, unvisited = [start], set(cities) - {start}
    while unvisited:
        nxt = min(unvisited, key=lambda c: dist[tour[-1]][c])
        tour.append(nxt)
        unvisited.remove(nxt)
    tour.append(start)
    return tour, tour_cost(tour)


print("All tours from A:")
tour, cost = tsp_brute_force('A')
print(f"\nOptimal tour : {' -> '.join(tour)}  (cost {cost})")
t2, c2 = nearest_neighbour('A')
print(f"Nearest neighbour heuristic: {' -> '.join(t2)}  (cost {c2})")
