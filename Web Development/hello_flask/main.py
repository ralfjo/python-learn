import time

# decorator - 다른 함수를 감싸는 함수로 함수에 기능을 더하거나 함수를 변형시킵니다.
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #Do somthing before
        function()
        function()
        #Do somthing after
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

def say_greeting():
    print("How are you?")

# say_greeting()
# say_hello()
decorated_function = delay_decorator(say_greeting)
decorated_function()
