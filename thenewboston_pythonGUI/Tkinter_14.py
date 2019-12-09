from tkinter import *

#Images and Icons
root = Tk()

photo = PhotoImage(file="mercedes.png")
label = Label(root, image=photo) #Label içerisine yerleştirmen gerek
label.pack()


root.mainloop()