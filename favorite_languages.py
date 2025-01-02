favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

language = favorite_languages["sarah"].title()

print(f"Sarah's favorite language is {language}.")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

for name in favorite_languages.keys():
    print(name.title())

for name in favorite_languages:
    print(name.title())

friends = ["phil", "sarah"]
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if "erin" not in favorite_languages.keys():
    print("Erin, please take our poll!")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

people_to_take_the_poll = [
    "jen",
    "sarah",
    "edward",
    "phil",
    "erin",
    "jim",
    "jane",
    "joe",
    "jack",
    "sam",
    "rachel",
    "pheobe",
    "john",
]
for person in people_to_take_the_poll:
    if person in favorite_languages.keys():
        print(f"Thank you {person.title()} for taking the poll.")
    else:
        print(f"{person.title()}, please take our poll.")

favorite_languages = {
    "jen": ["python", "ruby"],
    "sarah": ["c"],
    "edward": ["ruby", "go"],
    "phil": ["python", "haskell"],
}

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"{name.title()}'s favorite language is {languages[0].title()}.")
