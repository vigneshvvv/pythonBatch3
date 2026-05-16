car_dic = {
    "brand" : "FORD",
    "model": "MUSTANG",
    "year": 2026
}

print(car_dic["model"])

print(car_dic.get("type"))

car_dic["model"] = "FIGO"
print(car_dic)

car_dic["color"] = "Red"
print(car_dic)

car_dic.pop("color")
print(car_dic)


del car_dic["year"]
print(car_dic)

# car_dic.clear()

for key, value in car_dic.items():
    print(f"{key} is {value}")