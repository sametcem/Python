from tkinter import *


class CemButtons:
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print Message", command = self.printMessage)
        self.printButton.pack(side = LEFT)

        self.quitButton = Button(frame, text="Quit!", command = frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("Wow! this actually worked!")


root = Tk()
b = CemButtons(root) # root master olarak göründü



root.mainloop()