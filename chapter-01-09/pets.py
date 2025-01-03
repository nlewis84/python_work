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

pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)

while "cat" in pets:
    pets.remove("cat")

print(pets)


def describe_pet(
    pet_name,
    animal_type="dog",
):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet("harry", "hamster")
describe_pet("willie", "dog")
describe_pet("hamster", "harry")
describe_pet(pet_name="harry", animal_type="hamster")
describe_pet(pet_name="harry")
describe_pet("willie")

