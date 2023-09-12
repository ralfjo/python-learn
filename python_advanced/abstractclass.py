# Abstract Base Class
from abc import ABC, abstractmethod

class Car(ABC):

    def start_engine(self):
        print("start...")
    
    @abstractmethod
    def turn_off_engine(self):
        raise NotImplementedError

# c = Car()

class Tesla(Car):
    def turn_off_engine(self):
        print("turning off....")

t = Tesla()
t.start_engine()
t.turn_off_engine()


from typing import List, Protocol

class Item(Protocol):
    quantity: float
    price: float

class Product:
    def __init__(self, name: str, quantity: float, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price

class Stock:
    def __init__(self, product_name, quantity, price):
        self.product_name = product_name
        self.quantity = quantity
        self.price = price

def calculate_total(items: List[Item]) -> float:
    return sum([item.quantity * item.price for item in items])

# calculate total a product list
total = calculate_total([
    Product('A', 10, 150),
    Stock('B', 5, 250)])

print(total)

# duck typing