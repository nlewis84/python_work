class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display information about the restaurant."""
        print(f"\n{self.restaurant_name.title()} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Simulate opening the restaurant."""
        print(f"{self.restaurant_name.title()} is now open!")

    def set_number_served(self, number_served):
        """Set the number of customers that have been served."""
        self.number_served = number_served
    
    def increment_number_served(self, customers_served):
        """Increment the number of customers served."""
        self.number_served += customers_served
    


restaurant = Restaurant("the mean queen", "pizza")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(430)
print(f"\nNumber served: {restaurant.number_served}")
restaurant.increment_number_served(125)
print(f"Number served: {restaurant.number_served}")

restaurant = Restaurant("ludvig's bistro", "seafood")
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(f"\nNumber served: {restaurant.number_served}")
restaurant.set_number_served(689)
print(f"Number served: {restaurant.number_served}")

restaurant = Restaurant("mango thai", "thai")
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(f"\nNumber served: {restaurant.number_served}")
restaurant.increment_number_served(200)
print(f"Number served: {restaurant.number_served}")
