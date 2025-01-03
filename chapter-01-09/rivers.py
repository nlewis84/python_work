rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "yangtze": "china",
    "mississippi": "usa",
}

for river, country in rivers.items():
    if country == "usa":
        print(f"The {river.title()} runs through {country.upper()}.")
    else:
        print(f"The {river.title()} runs through {country.title()}.")

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    if country == "usa":
        print(country.upper())
    else:
        print(country.title())
