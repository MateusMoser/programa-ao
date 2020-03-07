from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()

def popup():
    response = messagebox.askquestion('this is it','hello world')
    Label(root,text=response).pack()

#    if response:
 #       Label(root, text='vloce clicou sim').pack()
 #   else:
 #       Label(root, text='vloce clicou nao').pack()


Button(root,text='popup',command=popup).pack()



mainloop()