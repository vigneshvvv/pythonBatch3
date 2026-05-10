# for i in range(5):
#     print(i)

# for i in range(1,6):
#     print(i)    

# for i in range(20):
#     if(i == 11):
#         print("The number 11 reached")
#         break
#     print(i)

# for i in range(20):
#     if(i == 11):
#         print("The number 11 reached")
#         continue
#     print(i)

values = ["sathish", "abdul", "revanth"]

for name in values:
    if(name == "abdul"):
        print("The name exist")
    print(name)

name = "abdul"

for charc in name:
    print(charc)

num = [1,3,4]

for s in num:
    if(s == 2):
        print("The number found !")
        break
else:
    print("The number doesn't exist in the given list")    