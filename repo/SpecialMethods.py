class Book():
    def __init__(self,name,author,pagenumber,genre):
        print("init function")
        self.name = name
        self.author = author
        self.pagenumber = pagenumber
        self.genre = genre

    def __str__(self):
        return "Name: {}\nAuthor {}\nPage Number: {}\nGenre: {}".format(self.name,self.author,self.pagenumber,self.genre)

    def __len__(self):
        return self.pagenumber

    def __del__(self):
        print("Book is deleted...........")


b1 = Book("Istanbul Hatirasi","Ahmet Umit",561,"Polisiye")
print(b1)
print("//")
print(b1.__str__())
print(len(b1))

del b1


# diveintopython3.net/special-method-names.html
