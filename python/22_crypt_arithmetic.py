# Experiment 22: Crypt-Arithmetic problem  (SEND + MORE = MONEY)
from itertools import permutations


def solve(word1, word2, result):
    letters = sorted(set(word1 + word2 + result))
    if len(letters) > 10:
        return None
    first_letters = {word1[0], word2[0], result[0]}

    def value(word, mapping):
        n = 0
        for ch in word:
            n = n * 10 + mapping[ch]
        return n

    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        if any(mapping[c] == 0 for c in first_letters):
            continue
        if value(word1, mapping) + value(word2, mapping) == value(result, mapping):
            return mapping
    return None


if __name__ == "__main__":
    w1, w2, res = "SEND", "MORE", "MONEY"
    sol = solve(w1, w2, res)
    if sol:
        print("Letter assignment:", sol)
        v = lambda w: ''.join(str(sol[c]) for c in w)
        print(f"  {v(w1)}\n+ {v(w2)}\n------\n {v(res)}")
    else:
        print("No solution")
