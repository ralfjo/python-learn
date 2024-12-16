class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False
        
def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")
    
new_user = User("ralfjo")
new_user.is_logged_in = True
create_blog_post(new_user)



# 고급 데코레이터
# 호출된 함수의 이름, 주어진 인수 및 마지막으로 반환된 출력을 출력할 logging_decorator()를 생성하세요:

# You called a_function(1,2,3) 
# It returned: 6 
# 값 6은 함수의 반환 값입니다.

# a_function의 본문을 변경하지 마세요.

# 중요: 이 연습에서는 *args만 사용하면 되며 **kwargs는 무시해도 됩니다.

def logging_decorator(func):
    def wrapper(*args):
        print(f"You called {func.__name__}{args}")
        result = func(*args)
        print(f"It returned: {result}")
        return result
    return wrapper

@logging_decorator
def a_function(*args):
    return sum(args)
    
a_function(1,2,3)