from random import randint


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)


# Create a 6-sided die and roll it 10 times.
die = Dice()

results = []
for roll_num in range(10):
    result = die.roll()
    results.append(result)
    print(f"Roll {roll_num + 1}: {result}")

print(f"\nResults: {results}\n")

# Create a 10-sided die and a 20-sided die. Roll each die
# 10 times.
die_10 = Dice(sides=10)
die_20 = Dice(sides=20)

results_10 = []
results_20 = []

for roll_num in range(10):
    result = die_10.roll()
    results_10.append(result)
    print(f"10-sided die roll {roll_num + 1}: {result}")

print(f"\nResults from 10-sided die: {results_10}\n")

for roll_num in range(10):
    result = die_20.roll()
    results_20.append(result)
    print(f"20-sided die roll {roll_num + 1}: {result}")

print(f"\nResults from 20-sided die: {results_20}\n")
