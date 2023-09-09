"""car.py"""

# class
class Car:
    # pass
    # initialize
    def __init__(self, color, engine_type):
        self.color = color
        self.engine_type = engine_type
        self.speed = 0
        self.is_start = False

    # method
    def start_engine(self):
        self.speed = 0
        self.is_start = True
    
    def speed_up(self, speed):
        self.speed += speed
    
    def speed_down(self, speed):
        self.speed -= speed