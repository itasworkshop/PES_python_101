
students = {"raj":75,"suraj":68,"Tom":87}
students_with_grade = {}

for i,j in students.items():
    score = j
    if score >=90 and score <=100:
        students_with_grade[i] = "A"
    elif score >=80 and score < 90:
        students_with_grade[i] = "b"
    elif score >=70 and score < 80:
        students_with_grade[i] = "C"
    else:
        students_with_grade[i] = "Failed"

print(students_with_grade)

