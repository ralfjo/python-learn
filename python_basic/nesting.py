usa = {
    "name": "USA",
    "continent": "North America"
}

south_korea = {
    "name": "South Korea",
    "continent": "East Asia"
}

countries = [
    usa,
    south_korea
]

for country in countries:
    print(country)
    print(country['name'])

california = ['los angeles', 'san francisco']
us_states = [california, "washington", "oregon"]
print(us_states)

countries = [
    us_states,
    south_korea
]
print(countries)