def sandwich(*toppings):
    print("\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print("- " + topping)


sandwich("ham", "cheese", "lettuce", "tomato")
sandwich("turkey", "bacon", "avocado", "onion", "mayo")
sandwich("roast beef", "swiss cheese", "lettuce", "tomato", "mustard")
