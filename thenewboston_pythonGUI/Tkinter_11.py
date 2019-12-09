from tkinter import *


def doNothing():
    print("Ok Ok I won't do....")

def showSettings():
    print("Settings are being shown...")

root = Tk()

# Creating the main menu
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

# Creating the ToolBar
toolbar = Frame(root, bg="blue")
insertButt = Button(toolbar, text="Insert Image", command=doNothing)
insertButt.pack(side=LEFT, padx =2,pady = 2 )  #padding is extra space
printButt = Button(toolbar, text="Print", command=showSettings)
printButt.pack(side=LEFT, padx =2,pady = 2 )
toolbar.pack(side=TOP,fill = X) #TOP menunun üzerine cıkarıcak,default menu top cünkü


#Adding Status Bar

status = Label(root, text="Preparing to do....", bd=1, relief=SUNKEN,anchor =W) #bd is Border ,relief -> how you want to appear this border w-West(text will appear in west)
status.pack(side=BOTTOM, fill=X)




root.mainloop()