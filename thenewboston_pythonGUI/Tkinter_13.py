from tkinter import *

#SHAPES AND GRAPHICS

root = Tk()

canvas = Canvas(root, width =200, height=100)
canvas.pack() # bu canvasin üzerine shape olusturacagiz

blackLine= canvas.create_line(0,0, 200,50,fill="blue") #baslangıc ve bitis coordinates x y olarak
redLine = canvas.create_line(0,100,200,50,fill ="red") # fill red -> make my line red

greenBox = canvas.create_rectangle(25,25,130,60,fill="green")

canvas.delete(redLine)
#canvas.delete(ALL)
root.mainloop()