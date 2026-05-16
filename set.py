# it dosen't allow duplicates
#it doen't values by index
# unordered

my_set = {"java", "java", "python", "JS"}


my_set.add("React")
print(my_set)

my_set.update(["React", "Angular"])
print(my_set)

my_set.remove("Angular")
print(my_set)

my_set.discard("Angular")
print(my_set)

# my_set.clear()
# print(my_set)

for x in my_set:
    print(x)