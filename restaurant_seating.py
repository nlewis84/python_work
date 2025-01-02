dinner = input("How many people are in your dinner group? ")
dinner = int(dinner)

if dinner > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")