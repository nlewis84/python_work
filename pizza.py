pizzas = ["pepperoni", "cheese", "sausage", "mushroom", "onion", "green pepper"]

for pizza in pizzas:
    print(f"I like {pizza} pizza.")

print("\nI really love pizza!")

pizzas.append("bacon")

friend_pizzas = pizzas[:]
friend_pizzas.append("ham")

print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"],
}

print(f"\nYou ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza["toppings"]:
    print(f"\t{topping}")