
fact(has_fever).
fact(has_cough).

rule(flu) :-
    fact(has_fever),
    fact(has_cough).

rule(needs_rest) :-
    rule(flu).

prove(X) :-
    fact(X).

prove(X) :-
    rule(X).

prove(X) :-
    rule(X),
    write('Proved: '),
    write(X),
    nl.
