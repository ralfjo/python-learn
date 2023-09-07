# key value
dic = {
    "country": "south korea",
    "city": "seoul",
    "gender": "male",
    "age" : 28
}

print(dic["country"])

for key, value in dic.items():
    print(f"{key}: {value}")

for key in dic:
    print(f"{key}: {dic[key]}")

print(list(dic.keys()))
print(dic.values())

# lookup key
print("name" in dic)
print("name" not in dic)

dic1 = {
    1: 1,
    2: 2
}
print(dic1[1])