magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print(
    f"Thank you, {magicians[0].title()}, {magicians[1].title()}, and {magicians[2].title()}! That was a great magic show!"
)

message = "Thank you, "
for i, magician in enumerate(magicians):
    if i == len(magicians) - 1:
        message += f"and {magician.title()}! "
    else:
        message += f"{magician.title()}, "

message += "That was a great magic show!"
print(message)

