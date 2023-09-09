# python 4 built-in data types
# List: [], mutable
# Dictionary: {}, mutable
# Set: {}, immutable
# Tuples: (), immutable

# List
my_list = [1,2,3]
my_list.append(4)
print(my_list)
my_list[1] = 0
print(my_list)

# Dictionary
my_dictionary = {
    "country": "south korea",
    "city": "seoul"
}
print(my_dictionary)
my_dictionary['country'] = "USA"
print(my_dictionary)

# Set
# it is unchangeable, but can add or remove
# cannot subscript
# unique
my_set1 = set((1,2,3))
print(my_set1)
my_set1.add(1)
print(my_set1)
l = [1,2,3,4,1,2,3,4]
print(l)
print(set(l))
print(list(set(l)))
my_set2 = {1,2,3}
print(my_set2)
my_set2.add(4)
print(my_set2)
my_set2.remove(4)
print(my_set2)

# Tuples
# Once it is created, you cannot change
# it is immutable
# Creation is faster than list
my_tuples = (1,2,3)
print(my_tuples[0])