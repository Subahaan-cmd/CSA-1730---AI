
fruit(apple).
fruit(banana).
fruit(grapes).
fruit(orange).
fruit(mango).

colour(apple, red).
colour(banana, yellow).
colour(grapes, green).
colour(orange, orange).
colour(mango, yellow).

fruit_colour(X, Y) :-
    fruit(X),
    colour(X, Y).
