pet_0 = {
    "type": "dog",
    "name": "buddy",
    "owner": "james",
}

pet_1 = {
    "type": "cat",
    "name": "whiskers",
    "owner": "jane",
}

pet_2 = {
    "type": "fish",
    "name": "goldie",
    "owner": "john",
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(f"{pet['name'].title()} is a {pet['type']} owned by {pet['owner'].title()}.")