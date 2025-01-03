# a dictionary about luke skywalker
person_0 = {
    "first_name": "Luke",
    "last_name": "Skywalker",
    "age": 23,
    "city": "Tatooine",
    "height": "5'7",
    "weight": "160 lbs",
    "hair_color": "blonde",
    "eye_color": "blue",
    "occupation": "Jedi Knight",
    "lightsaber_color": "green",
}

# for details in person:
#     print(f"{person[details]}")

for details in person_0.values():
    print(f"{details}")

person_1 = {
    "first_name": "Leia",
    "last_name": "Organa",
    "age": 23,
    "city": "Alderaan",
    "height": "5'1",
    "weight": "110 lbs",
    "hair_color": "brown",
    "eye_color": "brown",
    "occupation": "Princess",
}

person_2 = {
    "first_name": "Han",
    "last_name": "Solo",
    "age": 29,
    "city": "Corellia",
    "height": "5'11",
    "weight": "180 lbs",
    "hair_color": "brown",
    "eye_color": "brown",
    "occupation": "Smuggler",
}

people = [person_0, person_1, person_2]

for person in people:
    print(f"\n{person['first_name']} {person['last_name']}")
    print(f"\tAge: {person['age']}")
    print(f"\tCity: {person['city']}")
    print(f"\tHeight: {person['height']}")
    print(f"\tWeight: {person['weight']}")
    print(f"\tHair Color: {person['hair_color']}")
    print(f"\tEye Color: {person['eye_color']}")
    print(f"\tOccupation: {person['occupation']}")


def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {"first": first_name, "last": last_name, "age": age}
    return person


jedi_knight = build_person("obi-wan", "kenobi", 57)
print(jedi_knight)

