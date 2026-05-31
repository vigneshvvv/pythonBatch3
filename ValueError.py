
try:
    age = int(input("Enter a age: "))
    print(age)
except ValueError:
    print("please enter number only")
finally:
    print("program Completed")