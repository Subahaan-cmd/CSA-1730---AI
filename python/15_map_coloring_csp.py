# Experiment 15: Map Coloring as a Constraint Satisfaction Problem (backtracking)

variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
domains = {v: ['Red', 'Green', 'Blue'] for v in variables}
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q':  ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V':  ['SA', 'NSW'],
    'T':  [],
}


def is_consistent(var, color, assignment):
    return all(assignment.get(n) != color for n in neighbors[var])


def backtrack(assignment):
    if len(assignment) == len(variables):
        return assignment
    var = next(v for v in variables if v not in assignment)
    for color in domains[var]:
        if is_consistent(var, color, assignment):
            assignment[var] = color
            result = backtrack(assignment)
            if result:
                return result
            del assignment[var]
    return None


solution = backtrack({})
if solution:
    print("Map coloring solution:")
    for region, color in solution.items():
        print(f"  {region:4} -> {color}")
else:
    print("No solution exists")
