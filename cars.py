cars = ["bmw", "audi", "toyota", "subaru"]

cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)
print(sorted(cars))
print(cars)
cars.reverse()
print(cars)
print(len(cars))

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

