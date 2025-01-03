usernames = ["admin", "john", "jane", "joe", "jim"]

usernames = []
for username in usernames:
    if username == "admin":
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")

if not usernames:
    print("We need to find some users!")
else:
    for username in usernames:
        if username == "admin":
            print(f"Hello {username}, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")


current_users = ["admin", "john", "jane", "joe", "jim"]
new_users = ["jack", "sam", "rachel", "pheobe", "john", "jane", "JOHN"]

# lowercase version of current_users
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user}, that name is already taken.")
    else:
        print(f"Great, {new_user} is still available.")
