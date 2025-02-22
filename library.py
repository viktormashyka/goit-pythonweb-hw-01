from abc import ABC, abstractmethod
from typing import List
import logging

logging.basicConfig(level=logging.INFO)


class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year


class LibraryInterface(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass


class Library(LibraryInterface):
    def __init__(self) -> None:
        self.books: List[Book] = []


class LibraryManager:
    def __init__(self, library: Library) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: int) -> None:
        self.library.books.append(Book(title, author, year))
        logging.info(f"Book with title {title} added.")

    def remove_book(self, title: str) -> None:
        for book in self.library.books:
            if book.title == title:
                self.library.books.remove(book)
                logging.info(f"Book with title {title} removed.")
                break
        else:
            logging.info(f"Book with title {title} not found in library.")

    def show_books(self):
        if not self.library.books:
            logging.info("No books in library.")
            return

        logging.info(f'{"Title":<30} {"Author":<30} {"Year":<4}')
        logging.info("-" * 64)
        for book in self.library.books:
            logging.info(f"{book.title:<30} {book.author:<30} {book.year:<4}")


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
                logging.info("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
