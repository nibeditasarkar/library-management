# Library Management System

The given code represents a simple library management system implemented using a class called `Library`. The class has several methods to perform various operations related to managing books in the library. Let's go through the code and understand each part:

1. The `Library` class is defined. It has the following attributes:
   - `bookList`: A list to store the books in the library.
   - `name`: The name of the library.
   - `libraryCount`: The number of books in the library.
   - `lendDict`: A dictionary to keep track of the books that have been lent out, with the book name as the key and the borrower's name and serial number as the value.

2. The `_sortBooks` method is a helper method that sorts the book list in alphabetical order using the `sorted` function and a lambda function as the key.

3. The `displayBook` method prints the list of books in the library along with their authors.

4. The `lendBook` method allows a user to lend a book from the library. It checks if the requested book is available and updates the `lendDict` dictionary with the borrower's name and the serial number of the book.

5. The `addBook` method allows a user to add a new book to the library. The book is appended to the `bookList` and then sorted again using the `_sortBooks` method. The `libraryCount` is also incremented.

6. The `returnBook` method allows a user to return a book they have borrowed. It removes the book entry from the `lendDict` if it exists.

7. The `displayLendings` method prints the list of books that have been lent out along with the borrower's name and serial number.

8. The `displayLibraryCount` method prints the total number of books in the library.

9. The code block at the end checks if the code is being run as the main script and not imported as a module. It creates an instance of the `Library` class with an empty book list and a name. Then, it enters a while loop to display a menu of options to the user and performs the corresponding operations based on the user's choice.

   The available options are:
   - Display Book: Prints the list of books in the library.
   - Lend a Book: Allows the user to lend a book by providing the book name and their name.
   - Add a Book: Allows the user to add a book to the library by providing the book name and author's name.
   - Return a Book: Allows the user to return a book they have borrowed by providing the book name.
   - Display Lendings: Prints the list of books that have been lent out.
   - Display Library Count: Prints the total number of books in the library.

   After performing the selected operation, the user is prompted to either quit or continue using the library.
