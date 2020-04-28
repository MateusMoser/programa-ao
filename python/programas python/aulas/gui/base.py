from tkinter import *
from PIL import ImageTk,Image

root = Tk()


def open():
    top = Toplevel()
    label = Label(top, text='world').pack()

button = Button(root,text='open second windows',command=open)
button.pack()


mainloop()