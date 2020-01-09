from Bookstore import *

print("""***********************************

Welcome to BookStore!

Operations;

1. SHOW BOOKS

2. BOOK CHECK

3. ADD BOOK

4. DELETE BOOK

5. INCREASE PRINT NO

In order to quit, please type "q"
***********************************""")

kütüphane = Bookstore()

while True:
    oper = input("Operations to do:")

    if (oper == "q"):
        print("Programme is closing.....")
        break
    elif (oper == "1"):
        kütüphane.showBooks()

    elif (oper == "2"):
        name = input("Which book do you want to take a look? ")
        print("Book is searching...")
        time.sleep(2)

        kütüphane.checkBookByName(name)

    elif (oper == "3"):
        name = input("Name:")
        author = input("Author:")
        publisher = input("Publisher:")
        genre = input("Genre:")
        printNo = int(input("Print NO"))

        newBook = Book(name,author,publisher,genre,printNo)

        print("Book is being added....")
        time.sleep(2)

        kütüphane.addBook(newBook)
        print("Book is added, now available....")


    elif (oper == "4"):
        name = input("Which book do you want to delete ?")

        answer = input("Are you sure? (Y/N)")
        if (answer == "Y"):
            print("Book is removing...")
            time.sleep(2)
            kütüphane.deleteBook(name)
            print("Book completely removed....")


    elif (oper == "5"):
        name = input("Which print number of the book do you want to increase ?")
        print("Print No is increasing....")
        time.sleep(2)
        kütüphane.increasePrintNo(name)
        print("Print No Increased....")

    else:
        print("Invalid Operation...")




























