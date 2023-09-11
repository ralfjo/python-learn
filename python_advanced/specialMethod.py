# special, magic, dunder __xxx__

class Tesla(object):
    def __init__(self, owner, color):
        self.owner = owner
        self.color = color

    def __str__(self):
        return f"This is {self.color} color {self.owner}'s car"
    
    def __len__(self):
        return len(self.owner)
    
    def __del__(self):
        print("This car has been deleted")
    
    def __eq__(self, other):
        return self.color == other.color

tesla = Tesla("Joon", "White")
print(len(tesla))
# del tesla
# print(tesla) - Error

tesla = Tesla("Joon", "White")
tesla1 = Tesla("Aain", "White")
print(tesla == tesla1)
tesla2 = Tesla("Tera", "Blue")
print(tesla2 == tesla1)