from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry('150x400')

def show():
    mylabel = Label(root, text=var.get()).pack()

var = StringVar()

c = Checkbutton(root,text='CHECK',variable=var,onvalue='pizza',offvalue='hamburgur')
c.deselect()
c.pack()


button = Button(root,text='SHOW SELECTION',command=show)
button.pack()


root.mainloop()