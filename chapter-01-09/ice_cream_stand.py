from restaurants import Restaurant


class IceCreamStand(Restaurant):
    """Represent an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type="ice cream"):
        """Initialize attributes of the parent class."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display the flavors available."""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


ice_cream_stand = IceCreamStand("the big chill")
ice_cream_stand.flavors = [
    "vanilla",
    "chocolate",
    "black cherry",
    "strawberry",
    "mint chocolate chip",
]
ice_cream_stand.describe_restaurant()
ice_cream_stand.show_flavors()
