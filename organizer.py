#PLANNER FOR NOTES, CONTACTS AND TASKS
def add_contact(contacts):
    name = input("Enter contact name: ").lower()
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print("Contact added.")


def view_contacts(contacts):
    print("\nContacts:")
    if not contacts:
        print("No contacts available.")
    else:
        for name, phone in contacts.items():
            print(f"- {name.capitalize()}: {phone}")


def remove_contact(contacts):
    name = input("Enter contact name to remove: ").lower()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' has been removed.")
    else:
        print(f"Contact '{name}' not found.")


def add_note(notes):
    title = input("Enter note title: ").strip().capitalize()
    content = input("Enter note content: ").strip()
    notes[title] = content
    print("Note added.")


def view_notes(notes):
    print("\nNotes:")
    if not notes:
        print("No notes available.")
    else:
        for title, content in notes.items():
            print(f"- {title}: {content}")


def remove_note(notes):
    title = input("Enter note title to remove: ").strip().capitalize()
    if title in notes:
        del notes[title]
        print(f"Note '{title}' has been removed.")
    else:
        print(f"Note '{title}' not found.")


def add_task(tasks):
    desc = input("Add a description of a task: ").lower()
    tasks.append(desc)
    print("Task added.")


def view_tasks(tasks):
    print("\nTasks:")
    if not tasks:
        print("No tasks available.")
    else:
        for item in tasks:
            print(f"- {item}")


def remove_task(tasks):
    desc_removed = input("Add a description of a task to remove: ").lower()
    if desc_removed in tasks:
        tasks.remove(desc_removed)
        print("Task removed.")
    else:
        print("Task not in list.")


def contacts_menu():
    print("\nContacts Management")
    print("1. Add a contact")
    print("2. View all contacts")
    print("3. Remove a contact")
    print("4. Back to main menu")
    return int(input("\nChoose an option: "))


def notes_menu():
    print("\nNotes Management")
    print("1. Add a note")
    print("2. View all notes")
    print("3. Remove a note")
    print("4. Back to main menu")
    return int(input("\nChoose an option: "))


def tasks_menu():
    print("\nTasks Management")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Remove a task")
    print("4. Back to main menu")
    return int(input("\nChoose an option: "))


def main_menu():
    print("\nPersonal Organizer")
    print("1. Manage Contacts")
    print("2. Manage Tasks")  # Placeholder for future functionality
    print("3. Manage Notes")
    print("4. Exit")
    return int(input("\nChoose an option: "))


def handle_contact(contacts):
    option = contacts_menu()
    if option == 1:
        add_contact(contacts)
    elif option == 2:
        view_contacts(contacts)
    elif option == 3:
        remove_contact(contacts)
    elif option == 4:
        return
    else:
        print('Invalid option')

    handle_contact(contacts)


def handle_notes(notes):
    option = notes_menu()
    if option == 1:
        add_note(notes)
    elif option == 2:
        view_notes(notes)
    elif option == 3:
        remove_note(notes)
    elif option == 4:
        return
    else:
        print('Invalid option')

    handle_notes(notes)


def handle_tasks(tasks):
    while True:
        option = tasks_menu()
        if option == 1:
            add_task(tasks)
        elif option == 2:
            view_tasks(tasks)
        elif option == 3:
            remove_task(tasks)
        elif option == 4:
            break
        else:
            print("Invalid option. Please choose again.")


# notes_menu()

def main():
    contacts = {}
    notes = {}
    tasks = []

    while True:
        try:
            choice = main_menu()
            if choice == 1:
                handle_contact(contacts)
            elif choice == 2:
                handle_tasks(tasks)
            elif choice == 3:
                handle_notes(notes)

            else:
                print("Invalid option. Please choose again.")

        except ValueError:
            print("Invalid input. Please enter a number.")




main()
