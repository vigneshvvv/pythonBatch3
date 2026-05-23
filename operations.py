def operation(a, b, o):
    if(o == 1):
        return a +b
    elif (0 == 2):
        return a -b
    elif (o == 3):
        return a*b
    elif (o == 4):
        return a/b
    else :
        print("Invalid Operation please choose the right one")

def printOddOrEven(a):
    if(a % 2 == 0):
        print("The result is Even Number")
    else :
        print("The result number is ODD")


a = int(input("Enter Number A : "))
b = int(input("Enter number B : "))
c = int(input("Enter Operation to perform 1 : for Addition 2: Sub 3: Multiplication 4:Division"))
result = operation(a,b,c)
printOddOrEven(result)