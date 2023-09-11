# Data Types
# int, float, str, bool

#casting, dynamic typing

age: int = 0
name: str = "Hello"
height: float = 6.0
is_student: bool = True
print(name)

# Type hint
def enter_school(is_student: bool) -> bool:
    if is_student:
        return True
    else:
        return False
    
print(enter_school(is_student))