from abc import ABC, abstractmethod

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class LibraryInterface(ABC):
    @abstractmethod
    def __init__(self):
        pass

class Library(LibraryInterface):
    def __init__(self):
        self.books = []

class LibraryManager:
    def __init__(self, library):
        self.library = library

    def add_book(self, title, author, year):
        self.library.books.append(Book(title, author, year))
        print(f'Book with title {title} added.')

    def remove_book(self, title):
        for book in self.library.books:
            if book.title == title:
                self.library.books.remove(book)
                print(f'Book with title {title} removed.')
                break
        else:
            print(f'Book with title {title} not found in library.')

    def show_books(self):
        if not self.library.books:
            print("No books in library.")
            return
        
        print(f'{"Title":<30} {"Author":<30} {"Year":<4}')
        print('-' * 64)
        for book in self.library.books:
            print(f'{book.title:<30} {book.author:<30} {book.year:<4}')

def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

