
:- dynamic fact/1.

fact(has_fever).
fact(has_cough).

rule(flu) :-
    fact(has_fever),
    fact(has_cough).

rule(needs_rest) :-
    fact(flu).

forward :-
    rule(X),
    \+ fact(X),
    assertz(fact(X)),
    write('Derived fact: '),
    write(X),
    nl,
    forward.

forward :-
    write('Forward chaining completed.'),
    nl.
