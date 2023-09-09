from car import Car
# from car import CarCarCarCar as c
# as is for non-overlapping or short names

# Custom class
# naming convention
# PascalCase : class name
# camelCase : object name
# snake_case : anything else

# class
# class Car:
#     # pass
#     # initialize
#     def __init__(self, color, engine_type):
#         self.color = color
#         self.engine_type = engine_type
#         self.speed = 0
#         self.is_start = False

#     # method
#     def start_engine(self):
#         self.speed = 0
#         self.is_start = True
    
#     def speed_up(self, speed):
#         self.speed += speed
    
#     def speed_down(self, speed):
#         self.speed -= speed

# make instance
# tesla = Car("green", "electric")
tesla = Car(color="green", engine_type="electric")
# tesla = car.Car(color="green", engine_type="electric")
# insert attribute
# tesla.color = "red"
# tesla.engine_type = "electric"

# print(tesla.color)

# How to list all the attributes?
print(vars(tesla))

# constructor
# def __init__(self):


tesla.start_engine()
print(vars(tesla))
for i in range(1,100):
    tesla.speed_up(1)
    print(tesla.speed)

for i in range(1,100):
    tesla.speed_down(1)
    print(tesla.speed)
