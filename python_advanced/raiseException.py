# Raise Exception

# custom error (user defined error)
class GradeOutOfBoundError(Exception):
    def __init__(self, grade, message):
        print(grade)
        print(message)
        # do something error

try:
    grade = int(input("Type your score from 0 to 100: "))
    if grade < 0 or grade > 100:
        # raise ValueError("Grade should be between 0 to 100")
        # raise GradeOutOfBoundError(grade, "Grade should be between 0 to 100")
        raise GradeOutOfBoundError(
            grade=grade, 
            message="Grade should be between 0 to 100"
        )
except GradeOutOfBoundError:
    pass