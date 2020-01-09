import sqlite3

import time

class Book():
    def __init__(self,name,author,publisher,genre,printNo):

        self.name = name
        self.author = author
        self.publisher = publisher
        self.genre = genre
        self.printNo = printNo

    def __str__(self):
        return "Name of the Book: {}\nAuthor: {}\nPublisher: {}\nGenre: {}\nPrintNo: {}\n".format(self.name,self.author,self.publisher,self.genre,self.printNo)


class Bookstore():
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.con = sqlite3.connect("Bookstore.db")
        self.cursor = self.con.cursor()

        query = "Create Table If not exists BOOK (name TEXT,author TEXT,publisher TEXT,genre TEXT,printNo INT)"
        self.cursor.execute(query)

        self.con.commit()
    def close_connection(self):
        self.con.close()

    def showBooks(self):

        query =  "Select * From BOOK"
        self.cursor.execute(query)
        books = self.cursor.fetchall()

        if (len(books) == 0):
            print("There is no registered book in bookstore...")
        else:
            for i in books:
                book = Book(i[0],i[1],i[2],i[3],i[4])
                print(book)

    def checkBookByName(self,name):
        query = "Select * From BOOK where name = ?"
        self.cursor.execute(query,(name,))
        books = self.cursor.fetchall()

        if (len(books) == 0):
            print("There is no registered book in bookstore...")
        else:
            book = Book(books[0][0],books[0][1],books[0][2],books[0][3],books[0][4])
            print(book)

    def addBook(self,book):
        query = "Insert into BOOK Values(?,?,?,?,?)"
        self.cursor.execute(query,(book.name,book.author,book.publisher,book.genre,book.printNo))
        self.con.commit()

    def deleteBook(self,name):
        query = "Delete From BOOK where name = ?"
        self.cursor.execute(query,(name,))
        self.con.commit()

    def increasePrintNo(self,name):
        query = "Select * From BOOK where name = ?"
        self.cursor.execute(query,(name,))
        books = self.cursor.fetchall()

        if (len(books) == 0):
            print("There is no registered book in bookstore...")
        else:
            printNoX = books[0][4]
            printNoX += 1

            q2 = "Update BOOK set printNo = ? where name = ?"
            self.cursor.execute(q2,(printNoX,name))
            self.con.commit()

































