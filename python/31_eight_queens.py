# Experiment 31: 8-Queens Problem (backtracking)
N = 8
solutions = []


def is_safe(cols, row, col):
    for r in range(row):
        c = cols[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def place(cols, row):
    if row == N:
        solutions.append(cols[:])
        return
    for col in range(N):
        if is_safe(cols, row, col):
            cols.append(col)
            place(cols, row + 1)
            cols.pop()


place([], 0)
print(f"Total solutions for {N}-Queens: {len(solutions)}\n")
print("First solution (column of queen in each row):", solutions[0], "\n")
for col in solutions[0]:
    print(' '.join('Q' if c == col else '.' for c in range(N)))
