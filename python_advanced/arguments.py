def adding_numbers(*args):
    _sum = sum([arg for arg in args])
    return _sum

print(adding_numbers(1,2,3))

def concat_str(**kwargs):
    return "".join([kw for kw in kwargs])

print(concat_str(str1='a', str2='b', str3='c'))

def concat_str2(**kwargs):
    return "".join([kw for kw in kwargs.values()])

print(concat_str2(str1='a', str2='b', str3='c'))

lst = [1,2,3,4,5,6]
a, *b, c = lst
print(a)
print(b)
print(c)

# combine dictionarys
{**{"a": 1}, **{"b": 2}}