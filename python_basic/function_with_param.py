def travel():
    print("Hello there!")
    print("Are you excited?")

travel()

def travel_to_country(country: str):
    print("Hello there!")
    print(f"You are going to travel to {country}")
    print("Are you excited?")

# travel_to_country(country="USA")
travel_to_country("USA")

def travel_to_country(country: str, name: str):
    print(f"Hello {name}!")
    print(f"You are going to travel to {country}")
    print("Are you excited?")

# positional argument
# travel_to_country("USA", "Ralf")
travel_to_country(country="USA", name="Ralf")
