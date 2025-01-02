cities = {
    'santiago': {
        'country': 'chile',
        'population': 6_310_000,
        'fact': 'The city is named after Saint James.',
    },
    'paris': {
        'country': 'france',
        'population': 2_140_000,
        'fact': 'The Eiffel Tower is located in Paris.',
    },
    'tokyo': {
        'country': 'japan',
        'population': 13_515_271,
        'fact': 'Tokyo is the largest city in Japan.',
    },
}

for city, city_info in cities.items():
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']

    print(f"\n{city.title()} is in {country.title()}.")
    print(f"It has a population of about {population}.")
    print(f"{fact}")

prompt = "\nTell me the name of a city, and I'll tell you some information about it."
prompt += "\nEnter 'quit' to end the program.\n"

while True:
    city = input(prompt)
    city = city.lower()
    
    if city == 'quit':
        break
    elif city in cities:
        country = cities[city]['country']
        population = cities[city]['population']
        fact = cities[city]['fact']
        print(f"\n{city.title()} is in {country.title()}.")
        print(f"It has a population of about {population}.")
        print(f"{fact}")
    else:
        print(f"Sorry, I don't know anything about {city}.")