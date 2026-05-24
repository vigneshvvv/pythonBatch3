# file = open("demo.txt", "x")
# file.close()

# file = open("demo.txt", "w")
# file.write("Welcome to python class")
# file.close()

# file = open("demo.txt", "r")
# data = file.read()
# print(data)
# file.close()

# file = open("demo.txt", "a")
# file.write("\nnew text addded")
# file.close()

file = open("demo.txt", "r")

for line in file:
    print(line)

file.close()

