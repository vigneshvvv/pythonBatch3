
em = {
    "name": "arjun",
    "salary": 30000
}

try:
    print(em["age"])
except KeyError:
    print("The Key you are looking for doesn't exist")
    