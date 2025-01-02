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