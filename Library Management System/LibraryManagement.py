class Library:
    def __init__(self, filename="books.txt"):
        self.filename = filename
        self.file = open(self.filename, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        if not books:
            print("There is no book.")
        else:
            print("List of Books:")
            for book in books:
                book_info = book.strip().split(',')
                print(f"Title: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        book_name = input("Enter book title: ")
        author = input("Enter book author: ")
        release_date = input("Enter release year: ")
        num_pages = input("Enter number of pages: ")
        book_info = f"{book_name},{author},{release_date},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        book_name = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        books = self.file.readlines()
        updated_books = []
        removed = False
        for book in books:
            if book_name not in book:
                updated_books.append(book)
            else:
                removed = True
        if not removed:
            print("Book not found.")
        else:
            self.file.seek(0)
            self.file.truncate()
            for book in updated_books:
                self.file.write(book)
            print("Book removed.")


def main():
    lib = Library()

    while True:
        print("*** MENU***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        print("q) Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            lib.list_books()
        elif choice == "2":
            lib.add_book()
        elif choice == "3":
            lib.remove_book()
        elif choice == "q":
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()
