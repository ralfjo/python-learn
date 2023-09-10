# with open("sample1.txt") as f:
#     f.read()

# FileNotFoundError
try:
    with open("sample1.txt") as f:
        f.read()
except FileNotFoundError:
    print("FileNotFoundError occurs")

# KeyError
try:
    dict = {"k": "v"}
    print(dict['no'])
except KeyError as error_messages:
    print("KeyError occurs")
    print(error_messages)

# IndexError
try:
    country_list = ["USA","South korea","Japan"]
    pick_country = country_list[3]
except IndexError:
    print("IndexError occurs")

# TypeError
try:
    print(1 + "hello")
    dict = {"k": "v"}
    print(dict['no'])
except TypeError:
    print("TypeError occurs")
else:
    print("this got trggered due to no error found")
finally:
    print("always running this")

