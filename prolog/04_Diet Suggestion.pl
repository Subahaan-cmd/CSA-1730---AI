
food(fruits).
food(vegetables).
food(milk).
food(eggs).
food(rice).

diet(healthy, fruits).
diet(healthy, vegetables).
diet(healthy, milk).

diet(protein, eggs).
diet(protein, milk).

diet(energy, rice).
diet(energy, fruits).

suggest_diet(Type, Food) :-
    diet(Type, Food).
