cars = {
    "tesla": {
        "models": "sedan",
        "model3": "sedan",
        "modelx": "suv",
        "modely": "suv",
    }
}

from pprint import pprint
pprint(cars)
print(cars)

# walrus operator :=
(walrus := True)

num = [1,2,3,4,5]
description = {
    "length": (num_length := len(num)),
    "sum": (num_sum := sum(num)),
    "mean": num_sum / num_length,
}
print(description)

print("|" + "hello world".ljust(30) + "|")
print("|" + "hello world".rjust(30) + "|")
print("|" + "hello world".center(30) + "|") 


a = {"a": 1}
b = ["b"]
c = {1, 2, 3}

import pickle
with open("combine.pckl", "wb") as f:
    pickle.dump(a, f)
    pickle.dump(b, f)
    pickle.dump(c, f)

with open("combine.pckl", "rb") as f:
    x = pickle.load(f)
    y = pickle.load(f)
    z = pickle.load(f)

print(x)
print(y)
print(z)