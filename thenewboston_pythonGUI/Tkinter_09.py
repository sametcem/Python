from tkinter import *


def doNothing():
    print("Ok Ok I won't do....")

def showSettings():
    print("Settings are being shown...")

root = Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu,tearoff=0) #tearoff üstteki cizgileri sildi.
menu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="New Project....",command = doNothing)
subMenu.add_command(label="New...",command = doNothing)
subMenu.add_separator()
subMenu.add_command(label="Settings", command= showSettings)
subMenu.add_separator()
subMenu.add_command(label="Exit",command=quit)

editMenu=Menu(menu,tearoff=0)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

root.mainloop()