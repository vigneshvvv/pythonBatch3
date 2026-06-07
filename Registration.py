from users import users
from loginComponent import login

def register():
    userName = input("Enter your UserName: ")
    password = input("Enter your password: ")
    reEnter = input("ReEnter your password: ")

    if(password == reEnter):
        new_user = {
            "userName": userName,
            "password": password
        }
        users.append(new_user)
        print("User Registered successfully!")

        option = input("do you want to login ? 1.Yes 2.No")
        if(option == "1"):
            login()
