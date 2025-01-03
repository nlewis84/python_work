# pizzas = ["pepperoni", "cheese", "sausage", "mushroom", "onion", "green pepper"]

# for pizza in pizzas:
#     print(f"I like {pizza} pizza.")

# print("\nI really love pizza!")

# pizzas.append("bacon")

# friend_pizzas = pizzas[:]
# friend_pizzas.append("ham")

# print("\nMy favorite pizzas are:")
# for pizza in pizzas:
#     print(pizza)

# print("\nMy friend's favorite pizzas are:")
# for pizza in friend_pizzas:
#     print(pizza)

# pizza = {
#     "crust": "thick",
#     "toppings": ["mushrooms", "extra cheese"],
# }

# print(f"\nYou ordered a {pizza['crust']}-crust pizza with the following toppings:")
# for topping in pizza["toppings"]:
#     print(f"\t{topping}")


# def make_pizza(*toppings):
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print(f"\t{topping}")


# make_pizza("pepperoni")
# make_pizza("mushrooms", "green peppers", "extra cheese")


def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


# make_pizza(16, "pepperoni")
# make_pizza(12, "mushrooms", "green peppers", "extra cheese")
