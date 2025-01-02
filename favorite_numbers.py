favorite_numbers = {
    "jen": 7,
    "sarah": 3,
    "edward": 5,
    "phil": 9,
}

for numbers in favorite_numbers:
    print(f"{numbers.title()}'s favorite number is {favorite_numbers[numbers]}.")

favorite_numbers = {
    "jen": [7, 3, 5],
    "sarah": [3, 5, 7],
    "edward": [5, 7, 9],
    "phil": [9, 7, 5],
}

for numbers in favorite_numbers:
    if len(favorite_numbers[numbers]) > 1:
        print(f"{numbers.title()}'s favorite numbers are:")
        for number in favorite_numbers[numbers]:
            print(f"\t{number}")
    else:
        print(f"{numbers.title()}'s favorite number is {favorite_numbers[numbers][0]}.")