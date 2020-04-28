from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Dale')
root.iconbitmap('icone.ico')


#r = IntVar()
#r.set('2')

def clicked(value):
    mylabel = Label(root, text=value)
    mylabel.pack()

MODES = [
    ('pepperoni','pepperoni'),
    ('cheese','cheese'),
    ('mushroom','mushroom'),
    ('onion','onion'),
]

pizza =StringVar()
pizza.set('pepperoni')

for text,mode in MODES:
    Radiobutton(root,text=text,variable=pizza,value=mode).pack(anchor=W)


#Radiobutton(root,text='option 1',variable=r , value=1,command=lambda:clicked(r.get())).pack()
#Radiobutton(root,text='option 2',variable=r , value=2,command=lambda:clicked(r.get())).pack()

button = Button(root,text='click here',weight=1,command=lambda :clicked(pizza.get()))
button.pack()
#mylabel = Label(root,text=pizza.get())
#mylabel.pack()



root.mainloop()