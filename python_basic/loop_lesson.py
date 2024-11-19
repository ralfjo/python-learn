import random

# fruits = ["apple","peach","pear"]
# for fruit in fruits:
#     print(fruit)

# for number in range(1,46):
#     print(number)


# print(random.sample([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45], k=6))
# print(random.sample(range(1,46), k=6))


for number in range(1,101):
    if number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)