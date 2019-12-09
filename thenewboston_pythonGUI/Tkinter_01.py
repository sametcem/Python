# GUI Applications with Tkinter
from tkinter import * #everything in tkinter class

#VERY BASIC WINDOWS

root = Tk() #Nesne ürettik bu bir blink window.

theLabel = Label(root,text="Bu bir metin etiketi") #Text screen 1 where you want to put 2 text

theLabel.pack() #Rastgele bir yere koy.

root.mainloop() #Süreklilik için thousands of a second Infinite loop