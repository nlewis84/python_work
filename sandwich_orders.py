sandwich_orders = ["tuna", "pastrami", "chicken", "pastrami", "beef", "pastrami"]
finished_sandwiches = []

print("We have run out of pastrami.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nI have made the following sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
