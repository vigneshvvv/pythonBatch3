import json

username = "deva"
new_password = "deva"


with open("userDetails.json", "r") as file:
    users = json.load(file)

for user in users:
    if user["username"] == username:
        user["password"] = new_password


with open("userDetails.json", "w") as file:
    json.dump(users, file, indent=4)

print("password updated")