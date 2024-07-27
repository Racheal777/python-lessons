students = []


def add_student(name, age, grade):
    student = {
        "name": name,
        "age": age,
        "grade": grade
    }

    students.append(student)
    print('student has been added ')


def update_grade(name, new_grade):
    for student in students:
        if student["name"] == name:
            student["grade"] = new_grade
            print(f'f this {name} grade has been updated')
            return
    print(f" {name} is not in the list")


def calculate_average_grade():
    if len(students) == 0:
        print('no student added yet')
    else:
        grades = []

        for student in students:
            grades.append(student['grade'])
        total = sum(grades)

        average = total / len(students)
        students.append({"total_grade": total, "average_grade": average})
        print(f" Average grade is {average}")


def display_records():
    if len(students) == 0:
        print('no student added yet')
    for student in students:
        print(f" name is {student['name']}, age {student['age']}, grade {student['grade']}")


def main():
    while True:
        try:
            choice = int(
                input("Enter an option \n 1. Add a new student: \n 2. Update student:  \n 3. Calculate average "
                      "grade: \n 4. display all students : \n > "))
            if choice == 1:
                name = input("Enter Students name : ")
                age = int(input("Enter students age: "))
                grade = float(input("Enter students grade: "))
                add_student(name, age, grade)

            elif choice == 2:
                name = input("Enter Students name : ")

                grade = float(input("Enter students grade"))
                update_grade(name, grade)

            elif choice == 3:
                calculate_average_grade()

            elif choice == 4:
                display_records()

            elif choice == 5:
                print("Exiting the student directory")
                break
        except ValueError:
            print(f"input a correct number between 1 - 5")


main()
if __name__ == "__main__":
    main()
