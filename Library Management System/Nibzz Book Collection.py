#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Library:
    def __init__(self, bookList, name):
        self.bookList = self._sortBooks(bookList)  # Sort the book list initially
        self.name = name
        self.libraryCount = len(bookList)
        self.lendDict = {}

    def _sortBooks(self, bookList):
        # Sort the books in alphabetical order
        return sorted(bookList, key=lambda x: x[0].lower())

    def displayBook(self):
        print(f"I have the following books in my Collection: {self.name}")
        for i, book in enumerate(self.bookList):
            print(f"{i + 1}. {book[0]} by {book[1]}")

    def lendBook(self, user, book):
        for i, b in enumerate(self.bookList):
            if b[0].lower() == book.lower():
                if b[0] not in self.lendDict.keys():
                    self.lendDict[b[0]] = (user, i + 1)
                    print("Lender-Book database has been updated. You can take the book now.")
                else:
                    print(f"Book '{b[0]}' is already being used by {self.lendDict[b[0]][0]}")
                break
        else:
            print("Book not found in the library.")

    def addBook(self, book, author):
        self.bookList.append((book, author))
        self.bookList = self._sortBooks(self.bookList)  # Sort the book list again
        self.libraryCount += 1
        print("Book has been added to the booklist.")

    def returnBook(self, book):
        if book in self.lendDict.keys():
            del self.lendDict[book]
            print("Book has been returned.")
        else:
            print("Book is not currently lent out.")

    def displayLendings(self):
        print("Lendings:")
        for book, (user, serial_number) in self.lendDict.items():
            print(f"Book: {book} | Lender: {user} | Serial Number: {serial_number}")

    def displayLibraryCount(self):
        print(f"The library currently has {self.libraryCount} books.")

if __name__ == '__main__':
    nibzz = Library([], "Nibzz's Collection")

    while True:
        print(f"Welcome to {nibzz.name}. Enter your choice to continue.")
        print("1. Display Book")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        print("5. Display Lendings")
        print("6. Display Library Count")

        user_choice = input()
        if user_choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Please enter a valid option.")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            nibzz.displayBook()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend: ")
            user = input("Enter your name: ")
            nibzz.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add: ")
            author = input("Enter the author's name: ")
            nibzz.addBook(book, author)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return: ")
            nibzz.returnBook(book)

        elif user_choice == 5:
            nibzz.displayLendings()

        elif user_choice == 6:
            nibzz.displayLibraryCount()

        print("Press q to quit and c to continue")
        user_choice2 = ""
        while user_choice2 != "q" and user_choice2 != "c":
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue


# In[ ]:




