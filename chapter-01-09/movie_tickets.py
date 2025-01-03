# under 3 ticket is free, 3-12 ticket is 10, over 12 the ticket is 15
your_age = "Please enter your age: "
your_age += "\n(Enter 'quit' when you are finished.) "

age = 0
# while age != "quit":
#     age = input(your_age)
#     if age == "quit":
#         break
#     age = int(age)
#     if age < 3:
#         print("Your ticket is free!")
#     elif age < 13:
#         print("Your ticket is $10.")
#     else:
#         print("Your ticket is $15.")

active = True
while active:
    age = input(your_age)
    if age == "quit":
        break
    age = int(age)
    if age < 3:
        print("Your ticket is free!")
    elif age < 13:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")
