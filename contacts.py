contacts = {}


name = input(f"Add the name of the contact > ").lower()
phone = input(f"Add the phone number > ")
contact = {name: phone}
contacts.update(contact)
print(f"contact  added")


print("Contacts : ")
for name, phone in contacts.items():
    print(f" - {name.capitalize()} :  {phone}")


removed_contact = input(f"Add the name of the contact to remove > ").lower()

if removed_contact in contacts:
    print('hhhh')
    contacts.pop(removed_contact)
    print(f" contact with the name {removed_contact} has been removed")
else:
    print(f" contact with the name {removed_contact} doesnt exist")

print("Updated Contacts are : ")
for name, phone in contacts.items():
    print(f" - {name.capitalize()} :  {phone}")



tasks = []
desc = input(f"Add a description of a task > ").lower()
tasks.append(desc)

for item in tasks:
    print(item)

desc_removed = input(f"Add a description of a task to remove > ").lower()
if desc_removed in tasks:
    tasks.remove(desc_removed)
    print(f"item has been removed ")
else:
    print(f"item not in list ")


notes = {}
title = input(f"Add the name of the contact > ").lower()
content = input(f"Add the phone number > ")
note = {title: content}
notes.update(note)
print(f"contact  added")


print("Contacts : ")
for name, phone in notes.items():
    print(f" - {name.capitalize()} :  {phone}")


removed_note = input(f"Add the name of the contact to remove > ").lower()

if removed_note in notes:
    print('hhhh')
    notes.pop(removed_note)
    print(f" contact with the name {removed_note} has been removed")
else:
    print(f" contact with the name {removed_note} doesnt exist")

print("Updated Contacts are : ")
for title, content in notes.items():
    print(f" - {title.capitalize()} :  {content}")


menu = ['manage contact', 'manage task', 'manage note', 'exit']
for i in range(len(menu)):
    print(f"{i+1}. {menu[i]} ")

