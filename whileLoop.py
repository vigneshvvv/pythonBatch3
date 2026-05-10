count = 0

while count < 5:
    print(count)
    count+= 1
    

password = ""
attempts = 0
username = ""

while username != "vignesh" or password != "vignesh":
    username = input("Enter your username : ")
    password = input("Enter your password : ")
    attempts += 1
    if(attempts >= 3):
        print("Too many attemps. account locked")
        break
else:
    print("granted access")
