from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry('400x400')


def slide():
    label = Label(root,text=horizontal.get()).pack()
    root.geometry(str(horizontal.get())+ 'x'+ str(vertical.get()))


vertical = Scale(root, from_=100, to=400)
vertical.pack()
horizontal = Scale(root, from_=100, to=400, orient=HORIZONTAL)
horizontal.pack()
button = Button(root,text='clica aqui',command=slide).pack()





root.mainloop()
