
student(rajesh).
student(ravi).
student(priya).
student(anu).

teacher(john).
teacher(mary).
teacher(paul).

teaches(john, rajesh).
teaches(john, ravi).
teaches(mary, priya).
teaches(paul, anu).

student_teacher(Student, Teacher) :-
    student(Student),
    teaches(Teacher, Student).
