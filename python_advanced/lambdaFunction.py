# lambda expressions

# It is small anonymous function

# lambda arguments : expression

# def square(num):
#     return num**2

# print(square(3))

# lambda num : num**2

# square = lambda num: num**2
# print(square(3))

number_list = [1,2,3,4,5]
print(list(map(lambda num: num**2, number_list)))
print(list(filter(lambda num: num % 2 == 0, number_list)))