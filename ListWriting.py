names = ["vignesh", "Abdul", "Revanth"]

# with open("names.txt", "w") as file:
#     for name in names:
#         file.write(name + "\n")


with open("names.txt", "r") as file:
    data = file.readlines()

print(data)    
