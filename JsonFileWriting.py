import json

with open("userDetails.json", "r") as  file:
    users = json.load(file)


for user in users:
    print(user["username"])
