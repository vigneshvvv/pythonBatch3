import json

new_user = {
    "username": "deva",
    "password": "34213"
}

with open("userDetails.json", "r") as file:
    users = json.load(file)

users.append(new_user)

with open("userDetails.json", "w") as file:
    json.dump(users, file, indent=4)

print("user added")
