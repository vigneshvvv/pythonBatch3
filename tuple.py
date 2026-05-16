# A tuple is ordered and immutable 

mytuple = ("Mustang","Mustang", "Honda", 1964)

print(mytuple[0])
print(mytuple[-1])
print(mytuple[0:2])

y = list(mytuple)
y[2] = "BMW"
mytuple = tuple(y)

print(mytuple)

# del mytuple

# print(mytuple)

print(len(mytuple))

print(mytuple.count("Mustang"))

print(mytuple.index(1964))

