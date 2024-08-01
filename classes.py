# create a class
class Dog:
    name = 'Jack'
    breed = 'german shepherd'


# instantiate an object
my_dog = Dog()

print(my_dog.name)


class Car:
    tyres = '4 tyres'
    engine = "engine"
    seat = "seat"


ford = Car()
print(ford.tyres)


# assign properties to the object
class Person:
    color = "black"

    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person('Abi', 43)
print(f"name is {person1.name}, age is {person1.age}, complexion is {person1.color}")


class Student:
    school_name = "yn international"

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduce_self(self):
        return f"Hello my name is {self.name}, i am {self.age}. my school{self.school_name},  i am in grade {self.grade}"

    def get_grade(self):
        return self.grade


student1 = Student("richy", 24, 6)
student2 = Student("isaac", 25, 6)

print(student2.introduce_self())
print(student1.introduce_self())
print(student2.get_grade())
