from restaurants import Restaurant

restaurants = [
    Restaurant("the mean queen", "pizza"),
    Restaurant("ludvig's bistro", "seafood"),
    Restaurant("mango thai", "thai"),
]

for restaurant in restaurants:
    restaurant.describe_restaurant()
    restaurant.open_restaurant()
    print(f"\nNumber served: {restaurant.number_served}")
    restaurant.set_number_served(689)
    print(f"Number served: {restaurant.number_served}")
    restaurant.increment_number_served(200)
    print(f"Number served: {restaurant.number_served}")
    print("\n")
