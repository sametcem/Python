# Fitting Widgets in your Layout

from tkinter import *

root = Tk()

one = Label(root, text="One", bg ="red", fg="white") #bg - background fg - foreground so font
one.pack()
two = Label(root, text="Two", bg ="green", fg="black")
two.pack(fill=X) #grow wide as parent
three = Label(root, text="Three", bg ="blue", fg="white")
three.pack(side=LEFT, fill=Y)

root.mainloop()