# Experiment 24: Vacuum Cleaner Problem (two-room world, simple reflex agent)
import random

random.seed(7)


def reflex_vacuum_agent(location, status):
    if status == 'Dirty':
        return 'Suck'
    return 'Right' if location == 'A' else 'Left'


def run(steps=8):
    world = {'A': random.choice(['Clean', 'Dirty']), 'B': random.choice(['Clean', 'Dirty'])}
    location = random.choice(['A', 'B'])
    print("Initial:", world, "| Vacuum at", location)
    cost = 0
    for step in range(1, steps + 1):
        action = reflex_vacuum_agent(location, world[location])
        if action == 'Suck':
            world[location] = 'Clean'
        elif action == 'Right':
            location = 'B'
        else:
            location = 'A'
        cost += 1
        print(f"Step {step}: action={action:5} -> world={world}, vacuum at {location}")
        if all(v == 'Clean' for v in world.values()):
            print(f"\nBoth rooms are clean (actions taken: {cost}).")
            break


if __name__ == "__main__":
    run()
