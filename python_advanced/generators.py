# # what is generator?
# lazy iterator

# def get_cubes(n):
#     output = []
#     for x in range(n):
#         output.append(x**3)
#     return output

# print(get_cubes(5))


# for x in get_cubes(5):
#     print(x)


def get_cubes2(n):
    for x in range(n):
        yield x**3

print(get_cubes2(19))

for x in get_cubes2(5):
    print(x)

cubes = get_cubes2(5)
# print(cubes)

# returns the next item from the iterator
print(next(cubes))
print(next(cubes))
print(next(cubes))
print(next(cubes))
print(next(cubes))
# print(next(cubes)) # Error

s = "Joon"
# print(next(s))

# iter : convert object to iterator
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))