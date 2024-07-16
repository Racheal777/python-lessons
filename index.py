# Variables
AGE = 30
name = "Rachel"
AGE = '60'
Class = "lavender-python"

print(f"My name is {name}, I am  {AGE} years old and I am in {Class} class")

# Datatypes

text = 4447
my_age = int("34")
print(type(text))
print(type(my_age))

# DATATYPES
# CASTING IS CHANGING

person = ['john', 'M', 23, True, 120.8, 'john']
print(person[2])
print(person[-1])
# starts from index 1 - 4
print(person[1:5])
# prints everything in the array
print(person[:])

# print starting from the index 1
print(person[1:])

print(person[1:-1])

print(person[-4:5])

person[2] = 50
print(person)

# add an item to the end of the list
person.append('mumbai')
print(person)

# insert an item in the index
person.insert(3, 'Code')
print(person)

newList = [1, 2, 3]
# adds the new items at the end of the list
person.extend(newList)
print(person)

# remove item
person.remove('mumbai')
print(person)

n = person.pop(-1)
print(person)
print(n)

n = person.pop(3)
print(person)

# tuple
# remove an item from the end of a tuple
# ordered
# allows duplicate
# doesnt change
t = (1, 2, 3, 4, 5, 6)
r = list(t)
r.pop()
t = tuple(r)

print(t)

print(len(t))

fruits = ['apple', 'guava', 'banana', 'strawberry', 'pineapple', 'grapes', 'watermelon']
fruits.insert(2, 'mango')
print(fruits)

# fruits.pop(1)
# print(fruits)

num = [1, 2, 3, 4, 5, 6, 7]
print(num[0:6:2])

fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)

new = ['pear', 'orange']
# copy the values of fruits
newFruit = fruits.copy()
newFruit.extend(new)
print(fruits)
print(newFruit)

for fruit in fruits:
    print(fruit)

colors = ('#fffff', '0000', 'rrrrr')

#sets
# unordered, unindexed, unchangeable, no duplicate values

set1 = {1,1, True, 2, 3, 0, 4, 5, 6}
print(set1)

set1.add(False)
print(set1)
set1.pop()

print(set1)
#for item in set1:
    #print(item)