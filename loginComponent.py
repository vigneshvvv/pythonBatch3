from users import users

def login():

    userName = input("Enter your userName: ")
    password = input("Enter your password: ")

    for user in users:
        if(user["userName"] == userName and user["password"] == password):
            print("login successful")
            return
    print("Invalid username or password")