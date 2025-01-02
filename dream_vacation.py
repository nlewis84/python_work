vacation = "If you could visit one place in the world, where would you go?"
vacation += "\nPlease enter the name of a city you would like to visit: "
vacation += "\n(Enter 'quit' when you are finished.) "

hot_spots = []

while True:
    city = input(vacation)

    if city == "quit":
        break
    else:
        print(f"Adding {city} to your dream vacation list!")
        hot_spots.append(city)

print("\nHere is your dream vacation list:")

for city in hot_spots:
    print(city)