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


def car_info(manufacturer, model, **car_info):
    car = {}
    car["manufacturer"] = manufacturer
    car["model"] = model
    for key, value in car_info.items():
        car[key] = value
    return car


car = car_info("subaru", "outback", color="blue", tow_package=True)
print(car)
