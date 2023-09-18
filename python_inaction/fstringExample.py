a = 10
b = 20
print(f"{a = }, {b = }")

num = 100
print(f"num: {num:.2f}")
print(f"hex: {num:#0x}")
print(f"binary: {num:b}")
print(f"octal: {num:o}")
print(f"scientific: {num:e}")
print(f"Number: {num:09}")

num = 100000
print(f"{num = :,}")

percentage = 0.97444
print(f"{percentage = :.2%}")

import datetime
today = datetime.datetime.utcnow()
print(f"current : {today}")
print(f"current : {today:%m/%d/%Y %H:%M:%S}")

from dataclasses import dataclass
@dataclass
class Car:
    brand: str
    model: str

    def __str__(self) -> str:
        return f"{self.brand} has {self.model}"

model3 = Car("Tesla", "Model 3")
print(f"{model3}")
print(f"{model3!r}")


text = "Hello World"
print(f"{text :>50}")
print(f"{text :^50}")
print(f"{text :<50}")


country = "South Korea"
capital = "Seoul"
print(f"""
Country: {country :^30}
Country: {capital :^30}
""")