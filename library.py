class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        self.books.append(Book(title, author, year))

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                break
            else:
                print(f'Book with title {title} not found in library.')

    def show_books(self):
        if not self.books:
            print("No books in library.")
            return
        for book in self.books:
            print(f'Title: {book.title}, Author: {book.author}, Year: {book.year}')

def main():
    library = Library()
    
    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()
        
        if command == "add":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            year = input("Enter book year: ").strip()
            library.add_book(title, author, year)
        elif command == "remove":
            title = input("Enter book title to remove: ").strip()
            library.remove_book(title)
        elif command == "show":
            library.show_books()
        elif command == "exit":
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

