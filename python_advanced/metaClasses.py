# Metaclasses are just classes that create other classes

class Car(object):
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def __repr__(self):  # special method
        return f"Brand: {self.brand}, Color: {self.color}"

myTesla = Car("Tesla", "White")
print(myTesla)

# Python
# instances of the classes is considered objects, but also class is considered object

# print(type(myTesla))
# print(type(Car))

# EVCar = type('Car', (), {})
# print(EVCar())

# # Create additional method for our new Class
# def charge(self):
#     return "Charging up"

# EVCar = type('EVCar', (Car, ), {"batter_cap": "75KM", "charge": charge})
# print(EVCar)

# # Create Instance of EVCar called 'lucid'
# myLucid = EVCar('Lucid', 'Yellow')
# print(myLucid.brand)
# print(myLucid.color)
# print(myLucid.charge())
# print(myLucid.batter_cap)


# class Meta(type):
#     def __new__(self, name, bases, attrs):
#         return type(name, bases, attrs)

# Car = Meta('Car', (), {})
# print(Car)


class Meta(type):
    def __new__(self, name, attrs):
        attrs['shape'] = 'sedan'
        
        return type(name, (Car,), attrs)

EVCar = Meta('EVCar',{})

lucid = EVCar('Lucid', 'Yellow')

print(lucid)

print(lucid.shape)