#Organizing your layout

from tkinter import *

root = Tk()
topFrame = Frame(root) #Bir frame a atamam
topFrame.pack() #to display   ÜSTTEKİ DEFAULT ONE
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)

#Right now we have 2 frames
button1 = Button(topFrame, text="Button 1",fg="red") # fg is color
button2 = Button(topFrame, text="Button 2",fg="blue") # fg is color
button3 = Button(topFrame, text="Button 3",fg="green")
button4 = Button(bottomFrame, text="Button 4",fg="yellow")# fg is color


button1.pack(side = LEFT) #üret nereye koyacagını belirt ve ONAYLA
button3.pack(side = LEFT)
button2.pack(side = LEFT)

button4.pack(side = BOTTOM)



root.mainloop()