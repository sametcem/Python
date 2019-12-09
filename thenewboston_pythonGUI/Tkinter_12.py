from tkinter import *
import tkinter.messagebox

#MESSAGE BOX

root = Tk()

tkinter.messagebox.showinfo('Pencere basligi','Maymunlar 300 yasına kadar yasayabilir' )

answer= tkinter.messagebox.askquestion('Soru1','Adin Cem mi?')

if answer == 'yes':
    print('Merhaba Cem')
else:
    print('Lutfen adinizi giriniz')



root.mainloop()
