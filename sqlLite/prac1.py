import sqlite3

con = sqlite3.connect("Library.db")
cursor = con.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS BOOKSHELF (Name TEXT,Author TEXT,Publisher TEXT,Page_Number INT)")
    con.commit()
def insert_book():
    cursor.execute("INSERT INTO BOOKSHELF VALUES('İstanbul Hatirasi','Ahmet Umit','Everest',561)")
    con.commit()
def insert_book_byInput(name,author,publisher,page_number):
    cursor.execute("INSERT INTO BOOKSHELF VALUES(?,?,?,?)",(name,author,publisher,page_number))
    con.commit()
def getData():
    cursor.execute("SELECT * FROM BOOKSHELF")
    list = cursor.fetchall()
    print("---Bookshelf Data---")
    for i in list:
        print(i)
def getDataByName():
    cursor.execute("SELECT Name,Author FROM BOOKSHELF")
    list = cursor.fetchall()
    print("---Bookshelf Data---")
    for i in list:
        print(i)
def getDataByPublisher(publisher):
    cursor.execute("SELECT * FROM BOOKSHELF WHERE Publisher=?",(publisher,))
    list = cursor.fetchall()
    print("---Bookshelf Data---")
    for i in list:
        print(i)

def updatePublisher(oldPub,newPub):
    cursor.execute("UPDATE BOOKSHELF SET Publisher=? WHERE Publisher=?",(newPub,oldPub))
    con.commit()

def deleteByAuthor(aut):
    cursor.execute("DELETE FROM BOOKSHELF WHERE AUTHOR =?",(aut,))
    con.commit()


"""""
name = input("Name: ")
author = input("Author: ")
publisher = input("Publisher: ")
page_number = int(input("Page Number: "))
insert_book_byInput(name,author,publisher,page_number)
"""""

getData()
getDataByName()
getDataByPublisher('Everest')
updatePublisher("Everest","Mountain")
deleteByAuthor("Ahmet Umit")

con.close()


