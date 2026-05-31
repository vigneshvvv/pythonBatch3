names = ["new", "name"]

try:
    print(names[3])
except IndexError:
    print("The value doesn't exist for the index you have given")
except Exception as e:
    print(e)    