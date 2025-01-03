guests = ["Mark Lewis", "Thurman Leo Childs Jr.", "Paul Lewis"]

# print a message to each guest
print(f"Hello, {guests[0]}, I would like to invite you to dinner.")
print(f"Hello, {guests[1]}, I would like to invite you to dinner.")
print(f"Hello, {guests[2]}, I would like to invite you to dinner.")

cannot_make_it = guests.pop(2)
print(f"\n{cannot_make_it} cannot make it to dinner.")

# add a new guest to the list
guests.append("Dan Brown")
print(f"\nHello, {guests[0]}, I would like to invite you to dinner.")
print(f"Hello, {guests[1]}, I would like to invite you to dinner.")
print(f"Hello, {guests[2]}, I would like to invite you to dinner.")

print("\nI found a bigger table, so I can invite more people to dinner.")

# insert a new guest at the beginning of the list
guests.insert(0, "Gene Lewis")

# insert a new guest in the middle of the list
guests.insert(2, "James Lewis")

# append a new guest to the end of the list
guests.append("Charlie Childs")

print(f"\nHello, {guests[0]}, I would like to invite you to dinner.")
print(f"Hello, {guests[1]}, I would like to invite you to dinner.")
print(f"Hello, {guests[2]}, I would like to invite you to dinner.")
print(f"Hello, {guests[3]}, I would like to invite you to dinner.")
print(f"Hello, {guests[4]}, I would like to invite you to dinner.")
print(f"Hello, {guests[5]}, I would like to invite you to dinner.")

print(
    "\nMy table won't arrive in time for dinner, so I can only invite two people to dinner."
)
print("I can only invite two people to dinner.")

# count number of guests
number_of_guests = len(guests)
print(f"\nNumber of guests: {number_of_guests}")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"\n{removed_guest}, I'm sorry, but I can't invite you to dinner.")

print(f"\nNew number of guests: {len(guests)}")

print(f"\n{guests[0]}, you're still invited to dinner.")
print(f"{guests[1]}, you're still invited to dinner.")

del guests[0]
del guests[0]

print(f"\n{guests}")

