def gradeCalculator(score):
    if score >=80 and score <=100:
        return'A'
    elif score >=80 and score < 90:
        return'B'
    elif score >=70 and score < 80:
        return'C'
    else:
        return'F'

print(gradeCalculator(87))