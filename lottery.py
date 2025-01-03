# make a tuple of the first 5 numbers and 10 letters for the lottery
from random import choice

lottery_numbers_and_letters = (1, 2, 3, 4, 5, "a", "b", "c", "d", "e")

# randomly select 4 of these and print a message
winning_numbers_and_letters = []
for _ in range(4):
    winning_numbers_and_letters.append(choice(lottery_numbers_and_letters))

print("The winning lottery numbers and letters are:")
for number_or_letter in winning_numbers_and_letters:
    print(number_or_letter)

my_ticket = [1, 2, 3, 4]
print("\nMy ticket:")
for number_or_letter in my_ticket:
    print(number_or_letter)

# make a loop to see how many times the loop has to run to give me a winning ticket
attempts = 0
while True:
    ticket = []
    for number in range(4):
        ticket.append(choice(lottery_numbers_and_letters))
    if ticket == my_ticket:
        break
    attempts += 1

print(f"\nIt took {attempts} attempts to win the lottery.")
