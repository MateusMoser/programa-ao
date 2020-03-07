from tkinter import *
from PIL import ImageTk,Image


atual = 100
root = Tk()
root.geometry('100x'+ str(atual))



def show():
    mylabel = Label(root,text=var.get()).pack()
    atual += 30
    root.geometry('100x'+str(atual))


var = StringVar()
var.set('chose a date')

options = ['monday',
           'tuesday',
           'wednesday',
           'thursday',
           'friday']

drop = OptionMenu(root,var,*options)
drop.pack()

button = Button(root,text='show selection',command=show)
button.pack()

root.mainloop()