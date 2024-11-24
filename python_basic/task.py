# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice?")

# greet()

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")

# greet_with_name("Ralf")

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")

# greet_with("Ralf", "Nowhere")

# greet_with(location="Nowhere", name="Allen")

# def calculate_love_score(name1, name2):
    
#     check = name1 + name2
#     count1 = 0
#     count2 = 0
    
#     for char in check:
#         for true in "TRUE":
#             if char.lower() == true.lower():
#                 count1 += 1
        
#         for love in "LOVE":
#             if char.lower() == love.lower():
#                 count2 += 1
    
#     score = count1*10 + count2
    
#     print(f"Love Score = {score}")

# calculate_love_score(name1 = "Angela Yu", name2 = "Jack Bauer")

# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }

# print(travel_log["France"][1])

# nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][1])

# travel_log = {
#     "France": {
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12,
#     },
#     "Germany": {
#         "cities_visited": ["Stuttgart", "Berlin"],
#         "total_visits": 8,
#     }
# }

# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
    
#     return f"{formated_f_name} {formated_l_name}"

# formated_string = format_name("ralf", "jo")
# print(formated_string)

# def is_leap_year(year):
#     # """ Write your code here. 
#     #     Don't change the function name. """
#     if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#         leap_year = True
#     else:
#         leap_year = False
    
#     return leap_year

# def outer_function(a, b):
#     def inner_function(c, d):
#         return c + d
#     return inner_function(a, b)

# result = outer_function(5, 10)
# print(result)
