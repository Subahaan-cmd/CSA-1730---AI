
person(john, '2000-05-12').
person(mary, '2001-08-20').
person(paul, '2002-03-15').
person(lisa, '2003-11-25').
person(david, '2004-06-10').

display_dob(Name, DOB) :-
    person(Name, DOB).
