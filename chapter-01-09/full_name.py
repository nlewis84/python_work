first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"\n\tHello, {full_name.title()}!"
print(message)

print("\nLanguages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = ' python '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

nostarch_url = 'http://www.nostarch.com'
nostarch_url = nostarch_url.removeprefix('http://')
print(nostarch_url)