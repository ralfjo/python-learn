# static methods in Python are extremely similar to python class level methods,
# the difference being that a static method is bound to a class rather
# than the objects for that class. This means that a static method can be called
# without an object for that class. This also means that static methods cannot 
# modify the state of an object as they are not bound to it.

class Calc:
    def add(x: int, y: int) -> int:
        return x + y
    
# create addNumbers static method
Calc.add = staticmethod(Calc.add)

print('Product:', Calc.add(15,110))


class Calc2:
    @staticmethod
    def add(x: int, y: int) -> int:
        return x + y

print('Product:', Calc2.add(15,110))
