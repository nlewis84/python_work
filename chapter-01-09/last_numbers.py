for value in range(1, 21):
    print(value)

numbers = list(range(1, 1000001))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

# Odd Numbers
odd_numbers = list(range(1, 21, 2))
for value in odd_numbers:
    print(value)

# Threes
threes = list(range(3, 31, 3))
for value in threes:
    print(value)

# Cubes
cubes = []
for value in range(1, 11):
    cubes.append(value**3)
    print(value**3)

# Cubes Comprehension
cubes = [value**3 for value in range(1, 11)]
for value in cubes:
    print(value)
