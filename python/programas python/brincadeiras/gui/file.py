from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog


root = Tk()



def open():
    root.filename = filedialog.askopenfilename(initialdir='/gui', title='select a file',
                                               filetypes=(('png files', '*.png'), ('all files,', '*.*')))
    label = Label(root, text=root.filename)
    label.pack()
    global image
    image = ImageTk.PhotoImage(Image.open(root.filename))
    imagelabel = Label(image=image)
    imagelabel.pack()

meu_botao = Button(root,text='open file',command=open).pack()

root.mainloop()