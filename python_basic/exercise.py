student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

def get_grade(score):
    grade = ""
    
    if score > 90:
        grade = "Outstanding"
    elif score > 80:
        grade = "Exceeds Expectations"
    elif score > 70:
        grade = "Acceptable"
    else:
        grade = "Fail"
    
    return grade

for key in student_scores:
    student_grades[key] = get_grade(student_scores[key])

print(student_scores)
print(student_grades)