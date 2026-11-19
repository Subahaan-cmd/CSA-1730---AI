
symptom(ravi, fever).
symptom(ravi, cough).
symptom(ravi, headache).

symptom(rahul, fever).
symptom(rahul, cold).

disease(X, flu) :-
    symptom(X, fever),
    symptom(X, cough),
    symptom(X, headache).

disease(X, common_cold) :-
    symptom(X, cold),
    symptom(X, fever).

diagnosis(Person, Disease) :-
    disease(Person, Disease).
