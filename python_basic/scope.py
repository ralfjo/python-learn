# scope
# local scope / global scope / enclosed scope / enclosing scope
# namespace

my_score = 50

def inside_value_function():
    # global my_score
    my_score = 80
    print(f"my score inside is {my_score}")


inside_value_function()
print(f"my score outside is {my_score}")

did_extra_work = True
if did_extra_work:
    my_score = 90

print(f"my score outside is {my_score}")

# nonlocal
def a():
    x = 10
    def b():
        nonlocal x
        x = 20
    b()
    print(x)

a()

# How Python search the variable?
# (LEGB rule)
# 1. local
# 2. enclosing
# 3. global
# 4. built-in

## builtin namespace
# print(dir(__builtins__))

country = ["south korea"]

def inside_list_function():
    country.append("usa")
    # country = ["usa"]

inside_list_function()
print(country)

# globals keyword
print(globals())

# Global constant
HTTP_ENDPOINT = "https://yelp.com/"

def print_us_restaurant_url():
    print(f"{HTTP_ENDPOINT}/biz/arya-steakhouse-palo-alto")

def print_korean_restaurant_url():
    print(f"{HTTP_ENDPOINT}/biz/tobang-santa-clara-2")
