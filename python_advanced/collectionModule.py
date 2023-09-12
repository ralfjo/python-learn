from collections import Counter

lst = [1,2,3,2,2,2,3,3,3,3,1,1,1,1,1,2,2,2,3]
c = Counter(lst)
print(c)
print(dict(c))

c = Counter("hello")
print(c)

sentences = "hello world what a wonderful world"
c = Counter(sentences.split())
print(c)

# most common
print(c.most_common())

print(list(c))


# defaultdict never raises a KeyError
from collections import defaultdict
d = {'a':10}
print(d)

dd = defaultdict(lambda: 0)
dd['here'] = 10

print(dd['here'])

dd['there']
print(dd['there'])


from collections import namedtuple

t = (10,20,30)
print(t[1])

Dog = namedtuple('Dog', ['age','breed','name'])
print(Dog)
sammy = Dog(age=5, breed="Husky", name='Sammy')
print(sammy)
print(sammy.age)
print(sammy[0])