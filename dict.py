my_car = {"model": "Mercedes", "type": "Gle", "color": "red"}

car = dict(name="kofi", age=43)

print(my_car)
print(car)

model = my_car.get("model")
print(model)
color = my_car['color']
print(color)

# get keys
keys = my_car.keys()
print(keys)

# get values
values = my_car.values()
print(values)

items = my_car.items()
print(items)

# chane the value of the keys
my_car.update({"color": "black"})
print(my_car)

my_car["type"] = "saloon"

print(my_car)

# add new value to a dict
my_car["year"] = 2023

print(my_car)

new_car = dict(my_car, name="c677")

print(new_car)

# remove an item
my_car.pop('model')
print(my_car)

my_car.popitem()
print(my_car)

# student_directory = [
#     {
#         "id": 1,
#         "name": "Racheal",
#         "age": "20",
#         "class": "3"
#     },
#
# {
#         "id": 2,
#         "name": "Isaac",
#         "age": "20",
#         "class": "3"
#     }
# ]
student_directory = {}
student_1 = {
        "id": 1,
        "name": "Racheal",
        "age": "20",
        "class": "3"
    }

student_2 = {
        "id": 2,
        "name": "Isaac",
        "age": "20",
        "class": "3"
}

student_3 = {
        "id": 3,
        "name": "Ama",
        "age": "20",
        "class": "3"
}

student_directory["student_1"] = student_1
student_directory["student_2"] = student_2
student_directory["student_3"] = student_3

print(student_directory)
print(student_directory.keys())

for student in student_directory.values():
    print(student.get("name"))

