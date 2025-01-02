# conditional tests about call of cthulhu skills
skills = [
    "accounting",
    "anthropology",
    "archaeology",
    "art",
    "astronomy",
    "biology",
    "chemistry",
    "climb",
    "computer_science",
    "credit_rating",
    "fast_talk",
    "fighting",
    "firearms_handgun",
    "firearms_rifle",
    "firearms_shotgun",
    "firearms_submachine_gun",
    "first_aid",
    "history",
    "intimidate",
    "jump",
    "language_own",
    "language_other",
    "law",
    "library_use",
    "listen",
    "locksmith",
    "mech_repair",
    "medicine",
    "natural_world",
    "navigate",
    "occult",
    "op_hv_machine",
    "persuade",
    "pharmacy",
    "photography",
    "physics",
    "pilot",
    "psychoanalysis",
    "psychology",
    "ride",
    "sneak",
    "spot_hidden",
    "swim",
    "throw",
    "track",
]

# predict if a skill is in the list
print("I belive that 'accounting' is in the list.")
if "accounting" in skills:
    print("Accounting is in the list.")

# 4 more tests that evaluate true
print("\nI belive that 'anthropology' is in the list.")
if "anthropology" in skills:
    print("Anthropology is in the list.")

print("\nI belive that 'archaeology' is in the list.")
if "archaeology" in skills:
    print("Archaeology is in the list.")

print("\nI belive that 'art' is in the list.")
if "art" in skills:
    print("Art is in the list.")

print("\nI belive that 'astronomy' is in the list.")
if "astronomy" in skills:
    print("Astronomy is in the list.")

print("\nI belive that 'cthulhu mythos' is not in the list.")
if "cthulhu mythos" not in skills:
    print("Cthulhu Mythos is not in the list.")

# 4 more tests that evaluate false
print("\nI belive that 'disguise' is not in the list.")
if "disguise" not in skills:
    print("Disguise is not in the list.")

print("\nI belive that 'dodge' is not in the list.")
if "dodge" not in skills:
    print("Dodge is not in the list.")

print("\nI belive that 'drive auto' is not in the list.")
if "drive auto" not in skills:
    print("Drive Auto is not in the list.")

print("\nI belive that 'electrical repair' is not in the list.")
if "electrical repair" not in skills:
    print("Electrical Repair is not in the list.")

# Test for equality and inequality of strings
print("\nI belive that 'Accounting' is in the list.")
if "Accounting" in skills:
    print("Accounting is in the list.")

print("\nI belive that 'accounting' is not in the list.")
if "accounting" not in skills:
    print("Accounting is not in the list.")

# Test using the lower() method
print("\nI belive that 'Accounting' is in the list.")
if "Accounting".lower() in skills:
    print("Accounting is in the list.")

# Test using the and keyword
print("\nI belive that 'accounting' and 'anthropology' are in the list.")
if "accounting" in skills and "anthropology" in skills:
    print("Accounting and Anthropology are in the list.")
