import json

# p_list = ['foo', {'bar': ('baz', None, 1.0, 2)}]
# json_str = json.dumps(p_list)
# print("json_str: -----", json_str, ". Type of json_str is: -----", type(json_str))
# json_str_1 = '["foo", {"bar": ["baz", null, 1.0, 2]}]'
# print(json_str == json_str_1)
# p_list = json.loads(json_str_1)
# print("p_list: -----", p_list, ". Type of p_list is: -----", type(p_list))

# car = {
#     "brand": "Ford", "model": "Mustang", "year": 1964, "is_product": False,
#     "gear": {1: "<30", 2: "30-50", 3: "50-70", 4: "70>"}, "max_speed": 125.5,
#     "options": ["conditionar", "elctric window", "hard ceiling"], "color": None
# }
# car_l = json.dumps(car)
# print("car_l: -----", car_l, ". Type of car_l is: -----", type(car_l))
# car = json.loads(car_l)
# print("car: -----", car, ". Type of car is: -----", type(car))

# Data to be written
car = {
    "brand": "Ford", "model": "Mustang", "year": 1964, "is_product": False,
    "gear": {1: "<30", 2: "30-50", 3: "50-70", 4: "70>"}, "max_speed": 125.5,
    "options": ["conditionar", "elctric window", "hard ceiling"], "color": None
}

# Serializing json and
# Writing json file
with open("datafile.json", "w") as file:
    json.dump(car, file)

with open("datafile.json", "r") as file:
    json_car_data = json.load(file)

print("json_car_data: -----", json_car_data, ". Type of json_car_data is: -----", type(json_car_data))