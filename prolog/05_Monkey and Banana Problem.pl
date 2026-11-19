
% Initial state
initial_state(state(at(door), on_floor, at(window), has_not)).

% Monkey walks to the window
move(state(at(door), on_floor, B, has_not),
     walk,
     state(at(window), on_floor, B, has_not)).

% Monkey pushes the box to the middle
move(state(at(window), on_floor, at(window), has_not),
     push,
     state(at(middle), on_floor, at(middle), has_not)).

% Monkey climbs the box
move(state(at(middle), on_floor, at(middle), has_not),
     climb,
     state(at(middle), on_box, at(middle), has_not)).

% Monkey grasps the banana
move(state(at(middle), on_box, at(middle), has_not),
     grasp,
     state(at(middle), on_box, at(middle), has)).

% Goal condition
goal(state(_, _, _, has)).

% Solution
solve(State, []) :-
    goal(State).

solve(State, [Action|Rest]) :-
    move(State, Action, NextState),
    solve(NextState, Rest).
