favorite_places = {
    "jen": ["new york", "paris", "london"],
    "sarah": ["tokyo", "seoul", "beijing"],
    "edward": ["madrid", "barcelona", "lisbon"],
    "phil": ["rome", "athens", "berlin"],
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")
    print("\n")