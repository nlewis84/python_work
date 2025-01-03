glossary = {
    "list": "A collection of items in a particular order.",
    "dictionary": "A collection of key-value pairs.",
    "tuple": "An immutable list.",
    "if-elif-else": "A series of conditional tests.",
    "for loop": "A loop that iterates over a sequence of elements.",
    "while loop": "A loop that continues to execute as long as a condition is true.",
}

glossary["variable"] = "A placeholder for a value that can change."
glossary["string"] = "A series of characters."
glossary["integer"] = "A whole number."
glossary["float"] = "A number with a decimal point."
glossary["boolean"] = "A value that is either True or False."

for term, definition in glossary.items():
    print(f"\n{term.title()}:\n\t{definition}")
