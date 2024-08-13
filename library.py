
# LIBRARY MANAGEMENT SYSTEM
# 1. Add a Book
# 2. Remove a Book
# 3. Search for a Book
# 4. Display All books
# 5. Exit program


def loop_books(lists):
    for i in range(len(lists)):
        print(f'{i + 1}.  {lists[i]['title']}  writen by  {lists[i]['author']}')


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append({'title': title, 'author': author})
        print('book added successfully')
        return self.books

    def display_book(self):
        loop_books(self.books)

    def remove_book(self, title, author):
        for book in self.books:
            if book['title'] == title and book['author'] == author:
                self.books.remove(book)
                print(f"{title} has been removed")
                return
        print(f"{title} is not in the libray")

    def search_book(self, search):
        book_result = []
        for book in self.books:

            if book['title'].lower() == search.lower() or book['author'].lower() == search.lower():
                book_result.append(book)
                # print(f"{book['title']} by {book['author']} ")
        if book_result:
            print('Searched Book results')
            loop_books(book_result)
        else:
            print(f"{search} is not in the libray")


book = Library()

print("Choose an option")
print('1. Add a book')
print('2. Remove a book')
print('3. Display All books')
print('4. Search book')
print('5. Exit')

while True:
    try:
        choice = int(input("Choose an option > "))
        if choice == 1:
            title = input("Write the title of a book > ")
            author = input("Write the title of a book > ")
            book.add_book(title, author)
        elif choice == 2:
            title = input("Write the title of a book > ")
            author = input("Write the title of a book > ")
            book.remove_book(title, author)

        elif choice == 3:
            book.display_book()
        elif choice == 4:
            search = input("Write the title or author of a book to search > ")
            book.search_book(search)
        elif choice == 5:
            print('exited')
            break
        else:
            print('option is not allowed, choose again > ')
    except ValueError:
        print('please enter a valid')





