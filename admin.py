from user import User
from admin_user import Admin

admin = Admin("alovelace", "ada", "lovelace")
admin.describe_user()
admin.privileges.show_privileges()
print("\nAdding privileges...")
admin_privileges = [
    "can add post",
    "can delete post",
    "can ban user",
]
admin.privileges.privileges = admin_privileges
admin.privileges.show_privileges()
print("\nRemoving privileges...")
admin_privileges.remove("can ban user")
admin.privileges.privileges = admin_privileges
admin.privileges.show_privileges()

user = User("mcurie", "marie", "curie")
user.describe_user()
