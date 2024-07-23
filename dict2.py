solution1 = {
    "eben_home": 7808987,
    "eben_work": 9364556
}


for key, val in solution1.items():
    print(key, val)
print(solution1)

# for i in range(len(solution1)):
#     print(solution1)

solution2 = {"Eben": {
    "main_contact": 673445,
    "other_contact": 12345900
},
             "John": {
                "main_contact": 93948758,
             }
}

for key, val in solution2.get('Eben').items():
    print(key, val)

for key, val in solution2.items():
    print(key, val.values())



for key, val in solution2.items():
    print(key, val)

print(dir(solution1.items()))