toppings = "\nPlease enter the toppings you would like on your pizza: "
toppings += "\n(Enter 'quit' when you are finished.) "

while True:
    topping = input(toppings)

    if topping == 'quit':
        break
    else:
        print(f"Adding {topping} to your pizza!")