# assignment operator
# Assignment with an = on lists does not make a copy. Instead, assignment makes the two variables point to the one list in memory.
print("## assignment")
colors = ['red','blue','green']
b = colors
b.append('white')
print(b)
print(colors)

# shallow copy
# A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
print("## shallow copy")
a = [[1,2], [2,4]]
b = a[:] ## shallow copy
b.append([3,6])
print(b)
print(a)

b[0].append(3)
print(b)
print(a)

# deep copy
# A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.
print("## deep copy")
a = [[1,2], [2,4]]
import copy
b = copy.deepcopy(a)  ## deep copy
b[0].append(4)
print(b)
print(a)

# simple list
a = [1,2,3,4]
b = a[:]
b.append(5)
print(a)
print(b)


# reference
# https://medium.com/@thawsitt/assignment-vs-shallow-copy-vs-deep-copy-in-python-f70c2f0ebd86
