from tkinter import *

root = Tk()

def leftclick(Event):
    print('left')

def middleclick(Event):
    print('middle')

def rightclick(Event):
    print('right')

frame = Frame(root,width=300,height=200)
frame.bind('<Button-1>',leftclick)
frame.bind('<Button-2>',middleclick)
frame.bind('<Button-3>',rightclick)
frame.pack()

root.mainloop()