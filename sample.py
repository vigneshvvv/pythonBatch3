print("This is sample python execution")
print(10)
print(True) 

name = "vignesh"
print(type(name))

number = 100
print(type(number))

is_active = True
print(type(is_active))

per = 10.001
print(type(per))

# userName = input("Enter your UserName : ")
# password = input("Enter your password : ")

# print(userName, password)

# a = int(input("Enter number A : "))
# b = int(input("Enter number B : "))

# print(a+b)

userName = input("Enter your UserName : ")
password = input("Enter your password : ")

if(userName == "vignesh" and password == "vignesh"):
    print("The username and password matches")
else:
    print("Either username or password is incorrect")

a = int(input("Enter Number A : "))
b = int(input("Enter Number B : "))
c = int(input("Enter Operation you have to perform 1. Addition 2.sub 3.multiplication 4:Division : "))

if(c == 1):
    print(a+b)
elif(c == 2):
    print(a-b)
elif(c == 3):
    print(a*b)
elif(c == 4):
    print(a/b)
else:
    print("invalid operation please try again !")  
      
