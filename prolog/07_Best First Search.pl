
edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c, f).
edge(d, g).
edge(e, g).
edge(f, g).

heuristic(a, 6).
heuristic(b, 4).
heuristic(c, 3).
heuristic(d, 2).
heuristic(e, 5).
heuristic(f, 1).
heuristic(g, 0).

bestfirst(Start, Goal, Path) :-
    search([Start], Goal, [], RevPath),
    reverse(RevPath, Path).

search([Goal|_], Goal, Visited, [Goal|Visited]).

search([Current|Rest], Goal, Visited, Path) :-
    findall(H-Next,
        (edge(Current, Next),
         \+ member(Next, [Current|Visited]),
         heuristic(Next, H)),
        Candidates),
    keysort(Candidates, Sorted),
    pairs_values(Sorted, NextNodes),
    append(NextNodes, Rest, NewFrontier),
    search(NewFrontier, Goal, [Current|Visited], Path).
