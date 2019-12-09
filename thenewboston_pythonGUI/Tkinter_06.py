# Binding (baglamak) functions to layouts

from tkinter import *

root = Tk()

def printLeft(event):
    print("Left Click")

def printMiddle(event):
    print("Middle Click")
def printRight(event):
    print("Right Click")

button_1 = Button(root, text ="CheckButton" ) # command eklersen belirlerken () koyma.
button_1.bind("<Button-1>", printLeft)
button_1.bind("<Button-2>", printMiddle)
button_1.bind("<Button-3>", printRight)
button_1.pack()





root.mainloop()