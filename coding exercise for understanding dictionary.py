student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades={}
for thing in student_scores:
    if student_scores[thing] in range(0,70):
        student_scores[thing]="Fail"
    elif student_scores[thing] in range(71,80):
        student_scores[thing]="Acceptable"
    elif student_scores[thing] in range(81,90):
        student_scores[thing]="Exceeds Expectations"
    elif student_scores[thing] in range(91,100):
        student_scores[thing]="Outstanding"
    student_grades[thing]=student_scores[thing]
print(student_grades)    
