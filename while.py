#
# num = 1
# while num <= 7:
#     num += 1
#     print("I am less than 7")
#     if num == 4:
#         print("Oops i tricked you")
#         continue


st_database = {
    'isaac': 'python',
    'rich': 'javascript',
    'sarah': 'javascript'
}

password = "123"
entry = input("enter password > ")
while entry != password:
    entry = input("wrong password, try again > ")

print('Access granted')
print("Choose an option")
print('1.  remove an item')
print('2. update')
print('3. Print Database')
print('4. Exit')

while True:
    try:
        choice = int(input("Choose an option > "))
        if choice == 1:
            name = input("Choose a name to remove > ")
            st_database.pop(name)
            print(st_database)
            print('Database has been cleared')
        elif choice == 2:
            name = input("Enter name > ")
            Class = input("Enter class > ")

            st_database.update({name: Class})
            print('Successfully updated')
        elif choice == 3:
            print(st_database)
        elif choice == 4:
            print('All done')
            break
        else:
            print('option is not allowed, choose again > ')
    except ValueError:
        print('please enter a valid')
