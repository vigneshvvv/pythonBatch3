users = [
    {"username": "vignesh", "password": "vignesh"},
    {"username": "kumar", "password": "Kumar"},
    {"username": "abdul", "password": "abdul"}
]

enterd_user = input("Enter Username :")
entered_pass = input("Enter a password : ")

matches = False
for user in users:
    if user["username"] == enterd_user and user["password"] == entered_pass:
        matches = True
        break

if matches:
    print("logged in successfully")
else:
    print("Either username or password is incorrect")
