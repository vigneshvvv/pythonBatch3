users = [
    {"username": "vignesh", "password": "vignesh"},
    {"username": "kumar", "password": "Kumar"},
    {"username": "abdul", "password": "abdul"}
]



def checkLogin():
    attempts = 0

    while attempts < 3:
        userName = input("Enter your UserName : ")
        password = input("Enter your Password : ")
        found = False

        for data  in users:
            if(data["username"] == userName and data["password"] == password):
                found = True
                break
        if found:
            print("Login Succesfull")
            break
        else:
            attempts += 1
            print("Invalid credentials")
    if attempts == 3:
        print("Maximum attemts reached. Account Blocked !")


def registerNewUser():
    userName = input("Enter your UserName : ")
    password = input("Enter your password : ")
    reEnter = input("Re-Enter your password : ")
    exist = False

    for data in users:
        if data["username"] == userName and data["password"] == password:
            exist = True
            break                  
    if exist :
        print("userName aready exist please login")
    else :
        if password == reEnter:
            users.append({
                "username": userName,
                "password": password
            })
            print("Registration sucessful")
            print(users)
        else:
            print("password do not match")

def updatePassword():
    userName = input("Enter your username: ")
    oldPassword = input("Enter your old password : ")
    found = False

    for data in users:
        if data["username"] == userName and data["password"] == oldPassword:
            found = True
            newpassword = input("Enter your New Password : ")
            reEnter = input("Re-Enter your new Password : ")

            if newpassword == reEnter:
                data["password"] = newpassword
            else:
                print("passwords doesn't match")
            break
    if found:
        print(users)
    else :
        print("Invalid UserName or Old password")            


option = input("Enter operation you want to perform Login OR Register or updatePassword : ")

if option.lower() == "login":
    checkLogin()
elif option.lower() == "register":
    registerNewUser()
elif option.lower() == "updatepassword":
    updatePassword()
else :
    print("Invalid Operation please choose either register or login")    