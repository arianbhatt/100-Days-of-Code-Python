student_score={
        "Harry":81,
        "Ron":78,
        "Hermione":99,
        "Draco":74,
        "Neville":62
        }
student_grades={}
for student in student_score:
    if (student_score[student]>90):
        student_grades[student]="Outstanding"
    elif (student_score[student]>80):
        student_grades[student]="Exceeds Expectations"
    elif (student_score[student]>70):
        student_grades[student]="Acceptable"
    else:
        student_grades[student]="Fail"

print(student_grades)
 
