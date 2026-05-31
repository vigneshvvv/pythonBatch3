
with open("employees.txt", "r") as file:
    data = file.read()

names = data.split(",")
print(names)
names.append("Arun")

with open("employees.txt", "w") as file:
    file.write(",".join(names))